from decomp_recomp import *
from GPT_tools import *
from parser_tools import *
from api_tools import *

def main():
    while(True):
        # Get the question
        question = input("Please enter your question: ")
        try:
            # Initialize the models
            decomp_model = DecompGPT()
            recomp_model = RecompGPT()
            model_selector = ModelSelector()
            grammarParserModel = GrammarParser()
            divineBeastModel = AnswerModel()
            tools = ToolKit()
            manipulator = Manipulator()

            # get list of decomposed question
            response = decomp_model.getSubQuestions(question)

            # assign model to each sub question
            sub_questions = []
            [sub_questions.append((sub_question, manipulator.get_content(model_selector.getModel(sub_question)))) for sub_question in response]

            # Obtain the API requests to complete the sub answers
            sub_answers = [manipulator.get_content(divineBeastModel.getAnswer(sub_question, type)) for sub_question, type in zip(sub_questions)]

            # extract the API call from the sub question and apply tools to obtain sub_answers
            sub_answers = manipulator.use_tools(manipulator.extract_API_call(sub_answers), tools)

            # Reformat the sub_answers to the correct format
            sub_answers = manipulator.reformat_sub_answers(sub_answers, grammarParserModel)

            # recompile the sub_answers and main question into an answer and justification
            answer, justification = recomp_model.getRecomp(manipulator.recomposition_format(question, sub_answers))

            # print the answer and justification
            print("Answer: " + answer)
            print("Justification: " + justification)
        except Exception as e:
            print("Error: " + str(e))



if __name__ == "__main__":
    main()