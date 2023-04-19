import openai

class DecompGPT:
    def __init__(self):
        pass

    def getSubQuestions(self, question, max_tokens=750, token_info=False):
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "You are a helpful assistant that suggests sub-questions to help to answer a more complicated Question"},
                                                                                 {"role": "user", "content": "How do you find the integral of the function f(x) = e^(-2x) from 0 to infinity?"},
                                                                                 {"role": "assistant", "content": "\n1- What is the antiderivative of e^(-2x)? \n2- How do we evaluate an integral with limits from 0 to infinity? \n3- What is the value of the integral of e^(-2x) from 0 to infinity?"},
                                                                                 {"role": "user", "content": "Calculate the total resistance in a parallel circuit?"},
                                                                                 {"role": "assistant", "content": "1- How many resistors are there in the parallel circuit? \n2- What are the individual resistance values of each resistor? \n3- What formula is used to calculate total resistance for a parrallel circuit"},
                                                                                 {"role": "user", "content": "What is the area of a circle with a radius of 5?"},
                                                                                 {"role": "assistant", "content": "1- What is the formula for the area of a circle? \n2- How do you apply the formula with a radius of 5? \n3- What is the area of the circle?"},
                                                                                 {"role": "user", "content": "How do I find the limit of the function f(x) = (x^2 - 1) / (x - 1) as x approaches 1?"},
                                                                                 {"role": "assistant", "content": "1- What happens when you directly substitute x = 1 into the function? \n2- Can you simplify the function algebraically to find the limit? \n3- What is the limit of the function as x approaches 1?"},
                                                                                 {"role": "user",  "content": "Calculate the sum of the geometric series with a first term of 3, common ratio of 1/2, and 10 terms."},
                                                                                 {"role": "assistant",  "content": "1- What is the formula for the sum of a geometric series? \n2- How do you apply the formula with a first term of 3, common ratio of 1/2, and 10 terms? \n3- What is the sum of the geometric series?"},
                                                                                 {"role": "user", "content": "How many U.S. presidents have been assassinated while in office?"},
                                                                                 {"role": "assistant", "content": "1- Can you name all the U.S. presidents who have been assassinated? \n2- How many presidents does that make in total?"},
                                                                                 {"role": "user", "content": "Who was the first person to walk on the Moon?"},
                                                                                 {"role": "assistant", "content": "1- What was the name of the NASA mission that first landed humans on the Moon? \n2- Who were the astronauts involved in the mission? \n3- Who was the first person to walk on the Moon?"},
                                                                                 {"role": "user", "content": "What is the largest mammal on Earth?"},
                                                                                 {"role": "assistant", "content": "1- What are some countries with extensive coastlines? \n2- Which of these countries has the longest coastline when measured in kilometers or miles? \n3- What country has the longest coastline in the world?"},
                                                                                 {"role": "user", "content": "Which planet in our solar system has the most moons?"},
                                                                                 {"role": "assistant", "content": "1- What are the planets in our solar system? \n2- How many moons does each planet have? \n3- Which planet has the most moons?"},
                                                                                 {"role": "user", "content": "What is the oldest continuously inhabited city in the world?"},
                                                                                 {"role": "assistant", "content": "1- What is the oldest continuously inhabited city in the world?"},
                                                                                 {"role": "user", "content": "What is the smallest planet in our solar system?"},
                                                                                 {"role": "assistant", "content": "1- What is the smallest planet in our solar system?"},
                                                                                 {"role": "user", "content": "What is the speed of light in a vacuum?"},
                                                                                 {"role": "assistant", "content": "1- What is the speed of light in a vacuum?"},
                                                                                 {"role": "user", "content": "How do I find the volume of a cylinder with a radius of 4 and a height of 10?"},
                                                                                 {"role": "assistant", "content": "1- What is the formula for the volume of a cylinder? \n2- How do you apply the formula with a radius of 4 and a height of 10? \n3- What is the volume of the cylinder?"},
                                                                                 {"role": "user", "content": "How can I calculate the distance between two points on a coordinate plane?"},
                                                                                 {"role": "assistant", "content": "1- What are the coordinates of the two points? \n2- What is the formula for calculating the distance between two points on a coordinate plane? \n3- How do you apply the formula with the given coordinates? \n4- What is the distance between the two points?"},
                                                                                 {"role": "user", "content": question}], max_tokens=500)
        if token_info:
            print("Completion Tokents: " + str(response["usage"]["completion_tokens"]) + "Total tokens: " + str(response["usage"]["total_tokens"]))
        return response["choices"][0]["message"]["content"].split("\n"), response['usage']['total_tokens']


class RecompGPT:
    def __init__(self):
        pass

    def getRecomp(self, question, max_tokens=750, token_info=False):
        response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=[{"role": "system", "content": "You are a Devan a competent multi-hop question answering Language Model that provides well creafted a short answer with a chain of thought reasoning over facts provided alongside the question"},
                                                                                 {"role": "user", "content": "Question: How do I calculate the gradient of dL/dw given L = 1/exp(x),  x = 14y and y = 3.2w+b, b = 2, w = 4 \nFacts: The partial derivative of dL/dx = -1/exp(x). The partial derivative of dx/dy = 14. The partial gradient of dy/dw = 3.2. The derivative of dL/dW is equal to the multiplication of the partial derivatives evaluated at the point w = 4 and b = 2 dL/dw = dL/dx*dx/dy*dy/dw, x = 207.2"},
                                                                                 {"role": "assistant", "content": "The gradient is -4.62.\nReasoning: dL/dw = dL/dx*dx/dy*dy/dw = (-1/exp(x))*14*3.2 = -44.8/exp(x)\n x = 14y = 14(3.2w + b) = 14(3.2(4)+2) = 207.2\n -44.8/exp(207.2)=-4.62"},
                                                                                 {"role": "user", "content": "Question: What's the final amount of substance in the container after 2 hours? \nFacts: Initial substance is 1000 grams. Rate of change of substance follows a decay model with a decay constant of 0.3, which is represented by the equation dS/dt = -0.3S. To find the amount of substance after time t, the equation S(t) = S0 * exp(-kt) can be used, where S0 is the initial amount, k is the decay constant, and t is the time."},
                                                                                 {"role": "assistant", "content": "The final amount is 548.81 grams.\nReasoning: S(t) = S0 * exp(-kt) = 1000 * exp(-0.3 * 2) = 1000 * exp(-0.6) = 548.81"},
                                                                                 {"role": "user", "content": "Question: Which animal has a higher average lifespan, the Bowhead whale or the Galapagos tortoise? \nFacts: The Bowhead whale is a species of baleen whale which can live for more than 200 years, while the Galapagos tortoise is a species of tortoise native to the Galapagos Islands known to have lifespans exceeding 100 years, some reaching over 150 years. The average lifespan of a Bowhead whale is 211 years, whereas the average lifespan of a Galapagos tortoise is 137 years."},
                                                                                 {"role": "assistant", "content": "The Bowhead whale has a higher average lifespan.\nReasoning: The average lifespan of a Bowhead whale is 211 years, while the average lifespan of a Galapagos tortoise is 137 years. Since 211 > 137, the Bowhead whale has a higher average lifespan."},
                                                                                 {"role": "user", "content": "Question: Who was born first John or Jake? \nFacts John born in 1976 went to stephensons high school where he found the passion for the acting carreer he carefully crafted between 1996-2008, Jake is a proud astrophisicist we has help in the discovery of the first gravitationnal waves at the LIGO observatory he was born in 1974, The difference between Jake's birth date in 1974 and John's in 1976 is 2 years"},
                                                                                 {"role": "assistant", "content": "Jake was born First.\nReasoning: Jake was born in 1974 and John was born in 1976, 1974 < 1976, hence Jake was born first."},
                                                                                 {"role": "user", "content": question}], max_tokens=500)
        if token_info:
            print("Completion Tokents: " + str(response["usage"]["completion_tokens"]) + "Total tokens: " + str(response["usage"]["total_tokens"]))
        return response["choices"][0]["message"]["content"], response['usage']['total_tokens']