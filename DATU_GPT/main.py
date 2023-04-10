from DATU import *

def main():
    while(True):
        # Get the question
        question = input("Please enter your question: ")
        API_KEY = open("../../OpenAIApproach/OpenAIAPIKey.txt", "r").read()
        model = DATU(API_KEY)

        # model 1
        #answer1 = model.method_1_answer(question)
        #print(answer1)

        # model 2
        #answer2 = model.method_2_answer(question)
        #print(answer2)

        # model 3
        answer3 = model.method_3_answer(question)
        print(answer3)

        # base model
        answer4 = model.base_model_answer(question)
        print(answer4)



if __name__ == "__main__":
    main()