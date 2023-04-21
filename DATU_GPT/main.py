from DATU import *
from sql_wrapper import *

def main():
    # Get the question
    #question = input("Please enter your question: ")
    API_KEY = open("../OpenAIAPIKey.txt", "r").read()
    model = DATU(API_KEY)
    sql_script = Database(model)
    #sql_script.create_table()
    sql_script.fill_database("questions/fact_questions.csv")

    # model 1
    #answer0, subquestions, facts, tokens = model.method_decomp_answer(question)
    #print(answer0)

    # data_qa_tool
    #answer1, tokens, requests = model.method_data_qa_tool_answer(question)
    #print(answer1)

    # model math tool
    #answer2, tokens, requests = model.method_math_tool_answer(question)
    #print(answer2)

    # model 3
    #answer3, tokens, requests = model.method_complex_tool_answer(question)
    #print(answer3)

    # base model
    #answer4, tokens, requests = model.base_model_answer(question)
    #print(answer4)



if __name__ == "__main__":
    main()