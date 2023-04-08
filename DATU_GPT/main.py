from decomp_recomp import *
from GPT_tools import *
from parser_tools import *
from utils import *
from sql_wrapper import *

def main():
    while(True):
        # Get the question
        question = input("Please enter your question: ")

        # Initialize the models
        decomp_model = DecompGPT()
        recomp_model = RecompGPT()
        model_selector = ModelSelector()
        GrammarParserModel = GrammarParser()
        tools = ToolKit()
        manipulator = Manipulator()

        # get list of decomposed question
        response = decomp_model.getSubQuestions(question)

        # assign model to each subquestion
        sub_questions = []
        [sub_questions.append((sub_question, model_selector.getModel(sub_question))) for sub_question in response]

        # extract the API call from the subquestion and apply tools to obtain sub_answers
        sub_answers = manipulator.use_tools(manipulator.extract_API_call(sub_questions), tools)

        # recompile the sub_answers and main question into an answer and justification
        answer, justification = recomp_model.getRecomp(manipulator.recomposition_format(question, sub_answers))

        # print the answer and justification
        print("Answer: " + answer)
        print("Justification: " + justification)



if __name__ == "__main__":
    main()