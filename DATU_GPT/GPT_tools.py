import openai

class ModelSelector:
    def __init__(self):
        self.API_KEY = open("../../OpenAIApproach/OpenAIAPIKey.txt", "r").read()
        openai.api_key = self.API_KEY

    def getModel(self, question):
        return openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "You are an assistant is a classification model that classifies questions in order for them to be answered by one of four tools: Wiki, Math, QA, Human."},
                                                                             {"role": "user", "content": "Can you tell me about the history of the Taj Mahal?"},
                                                                             {"role": "assistant", "content": "[Wiki]"},
                                                                             {"role": "user", "content": "What is the square root of 64?"},
                                                                             {"role": "assistant", "content": "[Math]"},
                                                                             {"role": "user", "content": "What is the best way to learn a new language?"},
                                                                             {"role": "assistant", "content": "[QA]"},
                                                                             {"role": "user", "content": "What is your favorite movie?"},
                                                                             {"role": "assistant", "content": "[Human]"},
                                                                             {"role": "user", "content": "What is the definition of an adjective?"},
                                                                             {"role": "assistant", "content": "[Wiki]"},
                                                                             {"role": "user", "content": "How do I make pancakes from scratch?"},
                                                                             {"role": "assistant", "content": "[QA]"},
                                                                             {"role": "user", "content": "What is the population of Tokyo?"},
                                                                             {"role": "assistant", "content": "[Wiki]"},
                                                                             {"role": "user", "content": "What is the value of e?"},
                                                                             {"role": "assistant", "content": "[Math]"},
                                                                             {"role": "user", "content": "What is the meaning of life?"},
                                                                             {"role": "assistant", "content": "[QA]"},
                                                                             {"role": "user", "content": "What is your favorite color?"},
                                                                             {"role": "assistant", "content": "[Human]"},
                                                                             {"role": "user", "content": "Can you explain the process of photosynthesis?"},
                                                                             {"role": "assistant", "content": "[Wiki]"},
                                                                             {"role": "user", "content": "What is the sum of 2+2?"},
                                                                             {"role": "assistant", "content": "[Math]"},
                                                                             {"role": "user", "content": "What are the symptoms of COVID-19?"},
                                                                             {"role": "assistant", "content": "[QA]"},
                                                                             {"role": "user", "content": "What is your favorite book?"},
                                                                             {"role": "assistant", "content": "[Human]"},
                                                                             {"role": "user", "content": "What is the capital of France?"},
                                                                             {"role": "assistant", "content": "[Wiki]"},
                                                                             {"role": "user", "content": "How can I improve my writing skills?"},
                                                                             {"role": "assistant", "content": "[QA]"},
                                                                             {"role": "user", "content": "What is the height of Mount Everest?"},
                                                                             {"role": "assistant", "content": "[Wiki]"},
                                                                             {"role": "user", "content": "What is the value of pi?"},
                                                                             {"role": "assistant", "content": "[Math]"},
                                                                             {"role": "user", "content": "What is the difference between affect and effect?"},
                                                                             {"role": "assistant", "content": "[QA]"},
                                                                             {"role": "user", "content": "What is your favorite type of music?"},
                                                                             {"role": "assistant", "content": "[Human]"},
                                                                             {"role": "user", "content": question}], max_tokens=500)