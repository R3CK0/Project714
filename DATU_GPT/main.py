from DATU import *

def main():
    while(True):
        # Get the question
        question = input("Please enter your question: ")
        API_KEY = open("../../OpenAIApproach/OpenAIAPIKey.txt", "r").read()
        model = DATU(API_KEY)



if __name__ == "__main__":
    main()