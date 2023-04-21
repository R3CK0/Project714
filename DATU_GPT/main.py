from DATU import *
from sql_wrapper import *

def main():
    # Get the question
    #question = input("Please enter your question: ")
    API_KEY = open("../OpenAIAPIKey.txt", "r").read()
    model = DATU(API_KEY)
    #sql_script = Database(model)
    #sql_script.fill_database("questions/fact_questions.csv")
    model_choice = int(input("Please choose a model: \n1 - Method decomposition model\n2 - Data QA model\n3 - Math model\n4 - Complex model\n5 - Base model\n"))
    verbose = int(input("Please choose a verbosity level: \n0 - Just answer\n1 - intermittent subquestions and answers\n2 - Number of tokens and requests\n"))
    question = input("Please enter your question: ")
    # Method decomposition model
    if model_choice == 1:
        answer, decompositions, facts, tokens, requests = model.method_decomp_answer(question)
        if verbose == 0:
            print("Answer:" + str(answer))
        elif verbose == 1:
            print("Answer: " + str(answer) + "\nSubquestions: " + str(decompositions) + "\nSubanswers: " + str(facts))
        elif verbose == 2:
            print("Answer: " + str(answer) + "\nSubquestions: " + str(decompositions) + "\nSubanswers: " + str(facts) + "\nTokens used: " + str(tokens) + "\nRequests made: " + str(requests))

    # Data QA model
    elif model_choice == 2:
        subanswers, answers, tokens, requests = model.method_data_qa_tool_answer(question)
        if verbose == 0:
            print("Answer:" + str(answers))
        elif verbose == 1:
            print("Answer: " + str(answers) + "\nSubanswers: " + str(subanswers))
        elif verbose == 2:
            print("Answer: " + str(answers) + "\nSubanswers: " + str(subanswers) + "\nTokens used: " + str(tokens) + "\nRequests made: " + str(requests))

    # Math model
    elif model_choice == 3:
        subanswers, answers, tokens, requests = model.method_math_tool_answer(question)
        if verbose == 0:
            print("Answer:" + str(answers))
        elif verbose == 1:
            print("Answer: " + str(answers) + "\nSubanswers: " + str(subanswers))
        elif verbose == 2:
            print("Answer: " + str(answers) + "\nSubanswers: " + str(subanswers) + "\nTokens used: " + str(
                tokens) + "\nRequests made: " + str(requests))

    # Complex model
    if model_choice == 4:
        answer, decompositions, subanswers, facts, tokens, requests = model.method_complex_tool_answer(question)
        if verbose == 0:
            print("Answer:" + str(answer))
        elif verbose == 1:
            print("Answer: " + str(answer) + "\nSubquestions: " + str(decompositions) + "\nSubanswers: " + str(subanswers) + "\nFacts: " + str(facts))
        elif verbose == 2:
            print("Answer: " + str(answer) + "\nSubquestions: " + str(decompositions) + "\nSubanswers: " + str(subanswers) + "\nFacts: " + str(facts) + "\nTokens used: " + str(tokens) + "\nRequests made: " + str(requests))


    # base model
    elif model_choice == 5:
        answers, tokens, requests = model.base_model_answer(question)
        if verbose == 0:
            print("Answer:" + str(answers))
        elif verbose == 1:
            print("Answer: " + str(answers))
        elif verbose == 2:
            print("Answer: " + str(answers) + "\nTokens used: " + str(tokens) + "\nRequests made: " + str(requests))



if __name__ == "__main__":
    main()