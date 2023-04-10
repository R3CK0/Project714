from decomp_recomp import *
from GPT_tools import *
from parser_tools import *
from api_tools import *
import openai

class DATU:
    def __init__(self, key: str):
        self.decomp_model = DecompGPT()
        self.recomp_model = RecompGPT()
        self.model_selector = ModelSelector()
        self.grammarParserModel = GrammarParser()
        self.divineBeastModel = AnswerModel()
        self.tools = ToolKit()
        self.manipulator = Manipulator()
        openai.api_key = key



    def method_1_answer(self, question):
        # get list of decomposed question
        response = self.decomp_model.getSubQuestions(question)

        # assign model to each sub question
        sub_questions = []
        [sub_questions.append((sub_question, self.manipulator.get_content(self.model_selector.getModel(sub_question)))) for
         sub_question in response]

        # Obtain the API requests to complete the sub answers
        sub_answers = [self.manipulator.get_content(self.divineBeastModel.getAnswer(sub_question, type)) for sub_question, type in
                       zip(sub_questions)]

        # extract the API call from the sub question and apply tools to obtain sub_answers
        sub_answers = self.manipulator.use_tools(self.manipulator.extract_API_call(sub_answers), self.tools)

        # Reformat the sub_answers to the correct format
        sub_answers = self.manipulator.reformat_sub_answers(sub_answers, self.grammarParserModel)

        # recompile the sub_answers and main question into an answer and justification
        answer, justification = self.recomp_model.getRecomp(self.manipulator.recomposition_format(question, sub_answers))
        return answer, justification

    def method_2_answer(self, question):
        # get list of decomposed question
        response = self.decomp_model.getSubQuestions(question)

        # assign model to each sub question
        sub_questions = []
        [sub_questions.append((sub_question, self.manipulator.get_content(self.model_selector.getModel(sub_question)))) for sub_question in response]

        # Obtain the API requests to complete the sub answers
        sub_answers = []
        facts = ""
        for sub_question, type in zip(sub_questions):
            sub_answers.append(self.manipulator.get_content(self.divineBeastModel.getAnswer("Facts: " + facts + "Question: " + sub_question, type)))
            facts = "\n".join(sub_answers)

        # extract the API call from the sub question and apply tools to obtain sub_answers
        sub_answers = self.manipulator.use_tools(self.manipulator.extract_API_call(sub_answers), self.tools)

        # Reformat the sub_answers to the correct format
        sub_answers = self.manipulator.reformat_sub_answers(sub_answers, self.grammarParserModel)

        # recompile the sub_answers and main question into an answer and justification
        answer, justification = self.recomp_model.getRecomp(self.manipulator.recomposition_format(question, sub_answers))
        return answer, justification

    def method_3_answer(self, question):
        # get list of decomposed question
        response = self.decomp_model.getSubQuestions(question)

        # Obtain the API requests to complete the sub answers
        sub_answers = self.manipulator.get_content(self.divineBeastModel.getAnswer(question + "\n" +response))

        # extract the API call from the sub question and apply tools to obtain sub_answers
        sub_answers = self.manipulator.use_tools(self.manipulator.extract_API_call(sub_answers), self.tools)

        # Reformat the sub_answers to the correct format
        sub_answers = self.manipulator.reformat_sub_answers(sub_answers, self.grammarParserModel)

        # recompile the sub_answers and main question into an answer and justification
        answer, justification = self.recomp_model.getRecomp(self.manipulator.recomposition_format(question, sub_answers))
        return answer, justification

    def traditional_answer(self, question):
        return openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "You are a helpfull question answering assistant"},
                                                                             {"role": "user", "content": question}], max_tokens=500)