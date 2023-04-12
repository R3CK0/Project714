from DATU import *
from sql_wrapper import *

def main():
    # Get the question
    #question = input("Please enter your question: ")
    API_KEY = open("../../OpenAIApproach/OpenAIAPIKey.txt", "r").read()
    model = DATU(API_KEY)
    sql_script = Database(model)
    #sql_script.create_table()
    sql_script.fill_database("fact_questions.csv")

    # model 1
    #answer0, subquestions, facts = model.method_decomp_answer(question)
    #print(answer0)

    # data_qa_tool
    #answer1 = model.method_data_qa_tool_answer(question)
    #print(answer1)

    # model math tool
    #nswer2 = model.method_math_tool_answer(question)
    #print(answer2)

    # model 3
    #answer3 = model.method_complex_tool_answer(question)
    #print(answer3)

    # base model
    #answer4 = model.base_model_answer(question)
    #print(answer4)



if __name__ == "__main__":
    main()