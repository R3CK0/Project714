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


class RecompGPT:
    def __init__(self):
        self.API_KEY = open("../OpenAIAPIKey.txt", "r").read()
        openai.api_key = self.API_KEY

    def getRecomp(self, question):
        responseRecomp = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=[{"role": "System", "Content": "You are a Devan a competent multi-hop question answering Language Model that provides well creafted a short answer with a chain of thought reasoning over facts provided alongside the question"},
                                                                                       {"role": "user", "content": "Question: How do I calculate the gradient of dL/dw given L = 1/exp(x),  x = 14y and y = 3.2w+b, b = 2, w = 4 \nFacts: The partial derivative of dL/dx = -1/exp(x). The partial derivative of dx/dy = 14. The partial gradient of dy/dw = 3.2. The derivative of dL/dW is equal to the multiplication of the partial derivatives evaluated at the point w = 4 and b = 2 dL/dw = dL/dx*dx/dy*dy/dw, x = 207.2, "},
                                                                                       {"role": "assistant", "content": "The gradient is -4.62.\nReasoning: dL/dw = dL/dx*dx/dy*dy/dw = (-1/exp(x))*14*3.2 = -44.8/exp(x)\n x = 14y = 14(3.2w + b) = 14(3.2(4)+2) = 207.2\n -44.8/exp(207.2)=-4.62"},
                                                                                       {"role": "user", "content": "Question: What's the final amount of substance in the container after 2 hours? \nFacts: Initial substance is 1000 grams. Rate of change of substance follows a decay model with a decay constant of 0.3, which is represented by the equation dS/dt = -0.3S. To find the amount of substance after time t, the equation S(t) = S0 * exp(-kt) can be used, where S0 is the initial amount, k is the decay constant, and t is the time."},
                                                                                       {"role": "assistant", "content": "The final amount is 548.81 grams.\nReasoning: S(t) = S0 * exp(-kt) = 1000 * exp(-0.3 * 2) = 1000 * exp(-0.6) = 548.81"},
                                                                                       {"role": "user", "content": "Question: Which animal has a higher average lifespan, the Bowhead whale or the Galapagos tortoise? \nFacts: The Bowhead whale is a species of baleen whale which can live for more than 200 years, while the Galapagos tortoise is a species of tortoise native to the Galapagos Islands known to have lifespans exceeding 100 years, some reaching over 150 years. The average lifespan of a Bowhead whale is 211 years, whereas the average lifespan of a Galapagos tortoise is 137 years."},
                                                                                       {"role": "assistant", "content": "The Bowhead whale has a higher average lifespan.\nReasoning: The average lifespan of a Bowhead whale is 211 years, while the average lifespan of a Galapagos tortoise is 137 years. Since 211 > 137, the Bowhead whale has a higher average lifespan."},
                                                                                       {"role": "user", "content": "Question: Who was born first John or Jake? \nFacts John born in 1976 went to stephensons high school where he found the passion for the acting carreer he carefully crafted between 1996-2008, Jake is a proud astrophisicist we has help in the discovery of the first gravitationnal waves at the LIGO observatory he was born in 1974, The difference between Jake's birth date in 1974 and John's in 1976 is 2 years"},
                                                                                       {"role": "assistant", "content": "Jake was born First.\nReasoning: Jake was born in 1974 and John was born in 1976, 1974 < 1976, hence Jake was born first."},
                                                                                       {"role": "user", "content": question}], max_tokens=500)


class QuestionAnswerGPT:
    def __init__(self):
        self.API_KEY = open("../OpenAIAPIKey.txt", "r").read()
        openai.api_key = self.API_KEY

    def getAnswer(self, question):
        return openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "You are a helpful assistant that answers questions"},
                                                                                {"role": "user", "content": question}], max_tokens=500)