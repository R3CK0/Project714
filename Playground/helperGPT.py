import openai
import ujson

class DecompGPT:
    def __init__(self):
        self.API_KEY = open("../OpenAIAPIKey.txt", "r").read()
        openai.api_key = self.API_KEY

    def getSubQuestions(self, question):
        return openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "You are a helpful assistant that suggests sub-questions to help to answer a more complicated Question"},
                                                                             {"role": "user", "content": "If I throw a baseball how far will it go?"},
                                                                             {"role": "assistant", "content": "1- How much force was placed into the throw? \n2- Are you in an open space? \n3- What angle did you throw the ball in?"},
                                                                             {"role": "user", "content": "If I kick this ball what will happen?"},
                                                                             {"role": "assistant", "content": "1- How hard are you going to kick the ball?\n2- What kind of surface are you kicking it on?\n3- Is the ball inflated properly?\n4- What kind of ball is it?\n5- Will someone be there to catch it or will it hit a wall or the ground?"},
                                                                             {"role": "user", "content": "Were Scott Derrickson and Ed Wood of the same nationality?"},
                                                                             {"role": "assistant", "content": "1- What nationality is Scott Derrickson? \n2- What nationality is Ed Wood?"},
                                                                             {"role": "user", "content": "What is Hierarchical Task Network"},
                                                                             {"role": "assistant", "content": "1- What are the main components of a Hierarchical Task Network? \n2- How is a Hierarchical Task Network used in artificial intelligence? \n3- What are the advantages of using a Hierarchical Task Network approach versus other methods? \n4- Can you provide an example scenario of how a Hierarchical Task Network might be used in practice?"},
                                                                             {"role": "user", "content": question}], max_tokens=750)

class QuestionAnswerGPT:
    def __init__(self):
        #self.API_KEY = open("../OpenAIAPIKey.txt", "r").read()
        self.API_KEY = open("../openaikey.txt", "r").read()
        openai.api_key = self.API_KEY

    def getAnswer(self, question):
        return openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "You are a helpful assistant that answers questions"},
                                                                                {"role": "user", "content": question}], max_tokens=500)