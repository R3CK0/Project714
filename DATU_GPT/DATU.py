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

    def method_decomp_answer(self, question):
        answer = ""
        tokens = 0
        requests = 2
        # get list of decomposed question
        response, token = self.decomp_model.getSubQuestions(question)
        tokens = tokens + token

        # Obtain the API requests to complete the sub answers
        sub_answers = []
        facts = ""
        for sub_question in response:
            answer, token = self.manipulator.get_content(self.divineBeastModel.getAnswer("Facts: " + facts + "Question: " + sub_question, "[Base]"))
            sub_answers.append(answer)
            facts = "\n".join(sub_answers)
            tokens = tokens + token
            requests = requests + 1

        # recompile the sub_answers and main question into an answer and justification
        answer, token = self.recomp_model.getRecomp(question +  "\n".join(sub_answers))
        tokens = tokens + token

        return answer, response, facts, tokens, requests

    def method_complex_tool_answer(self, question):
        # get list of decomposed question
        tokens = 0
        requests = 3
        responses, token = self.decomp_model.getSubQuestions(question)
        tokens = tokens + token

        # Obtain the API requests to complete the sub answers
        facts = "Main Question: " + question + "\n"
        answers = []
        for response in responses:
            sub_answer, token = self.manipulator.get_content(self.divineBeastModel.getAnswer(facts + "\nQuestion: " + response, self.model_selector.getModel(response)))
            answers.append(sub_answer)
            sub_answer = self.manipulator.extract_API_call(sub_answer)
            tokens = tokens + token
            facts = facts + "\nFact: " + sub_answer
            requests += 2
        # extract the API call from the sub question and apply tools to obtain sub_answers
        # Reformat the sub_answers to the correct format
        #sub_answers = self.manipulator.get_content(self.grammarParserModel.parse(facts))

        # recompile the sub_answers and main question into an answer and justification
        answer, token = self.recomp_model.getRecomp(facts)
        tokens = tokens + token
        # clear variables
        self.manipulator.clear_Toolkit()
        
        return answer, "\n".join(responses), "\n".join(answers), facts, tokens, requests

    def method_data_qa_tool_answer(self, question):
        answer, tokens = self.manipulator.get_content(self.divineBeastModel.getAnswer(question, "[QA]"))
        self.manipulator.clear_Toolkit()
        return answer, self.manipulator.extract_API_call(answer), tokens, 1

    def base_model_answer(self, question):
        answer, tokens = self.manipulator.get_content(self.divineBeastModel.getAnswer(question, "[Base]"))
        return answer, tokens, 1

    def method_math_tool_answer(self, equation):
        answer, tokens = self.manipulator.get_content(self.divineBeastModel.getAnswer(equation, "[Math]"))
        self.manipulator.clear_Toolkit()
        return answer, self.manipulator.extract_API_call(answer), tokens, 1
