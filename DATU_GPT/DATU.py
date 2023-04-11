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
        try:
            # get list of decomposed question
            response = self.decomp_model.getSubQuestions(question)

            # Obtain the API requests to complete the sub answers
            sub_answers = []
            facts = ""
            for sub_question in response:
                sub_answers.append(self.manipulator.get_content(self.divineBeastModel.getAnswer("Facts: " + facts + "Question: " + sub_question, "[Base]")))
                facts = "\n".join(sub_answers)

            # recompile the sub_answers and main question into an answer and justification
            answer = self.recomp_model.getRecomp(question +  "\n".join(sub_answers))
        except:
            print("Error in decomp recomp")

        return answer, response, facts

    def method_complex_tool_answer(self, question):
        # get list of decomposed question
        response = "\n".join(self.decomp_model.getSubQuestions(question))
        print(response)

        # Obtain the API requests to complete the sub answers
        sub_answers = self.manipulator.get_content(self.divineBeastModel.getAnswer(question + "\n" + response))
        print(sub_answers)

        # extract the API call from the sub question and apply tools to obtain sub_answers
        sub_answers = self.manipulator.extract_API_call(sub_answers)
        print(sub_answers)

        # Reformat the sub_answers to the correct format
        #sub_answers = self.manipulator.get_content(self.grammarParserModel.parse(sub_answers))

        # recompile the sub_answers and main question into an answer and justification
        answer = self.recomp_model.getRecomp("Question: " + question + "\nFacts: " + sub_answers)
        
        # clear variables
        self.tools.clear_toolKit()
        
        return answer

    def method_data_qa_tool_answer(self, question):
        answer = self.manipulator.get_content(self.divineBeastModel.getAnswer(question, "[Wiki]"))
        return answer

    def base_model_answer(self, question):
        answer = self.manipulator.get_content(self.divineBeastModel.getAnswer(question, "[Base]"))
        return answer

    def method_math_tool_answer(self, equation):
        answer = self.manipulator.get_content(self.divineBeastModel.getAnswer(equation, "[math]"))
        return self.manipulator.extract_API_call(answer)