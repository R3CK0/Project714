import openai

class ModelSelector:
    def __init__(self):
        pass

    def getModel(self, question):
        answer = None
        while answer != "[Wiki]" and answer != "[Math]" and answer != "[QA]" and answer != "[Human]":
            answer = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "You are a classification model that classifies questions by the type they should be answered by Wiki, Math, QA, Human. for example: "
                                                                                                                 "\nQuestion: Can you tell me about the history of the Taj Mahal?"
                                                                                                                 "\nAnswer: [Wiki]\n"
                                                                                                                 "\nQuestion: What is the square root of 64?"
                                                                                                                 "\nAnswer: [Math]\n"
                                                                                                                 "\nQuestion: What is the best way to learn a new language?"
                                                                                                                 "\nAnswer: [QA]\n"
                                                                                                                 "\nQuestion: What is your favorite movie?"
                                                                                                                 "\nAnswer: [Human]\n"
                                                                                                                 "\nQuestion: What is the definition of an adjective?"
                                                                                                                 "\nAnswer: [Wiki]\n"
                                                                                                                 "\nQuestion: How many representants are in the senate?"
                                                                                                                 "\nAnswer: [QA]\n"
                                                                                                                 "\nQuestion: What is the population of Tokyo?"
                                                                                                                 "\nAnswer: [QA]\n"},
                                                                                 # {"role": "user", "content": "Can you tell me about the history of the Taj Mahal?"},
                                                                                 # {"role": "assistant", "content": "[Wiki]"},
                                                                                 # {"role": "user", "content": "What is the square root of 64?"},
                                                                                 # {"role": "assistant", "content": "[Math]"},
                                                                                 # {"role": "user", "content": "What is the best way to learn a new language?"},
                                                                                 # {"role": "assistant", "content": "[QA]"},
                                                                                 # {"role": "user", "content": "What is your favorite movie?"},
                                                                                 # {"role": "assistant", "content": "[Human]"},
                                                                                 # {"role": "user", "content": "What is the definition of an adjective?"},
                                                                                 # {"role": "assistant", "content": "[Wiki]"},
                                                                                 # {"role": "user", "content": "How do I make pancakes from scratch?"},
                                                                                 # {"role": "assistant", "content": "[QA]"},
                                                                                 # {"role": "user", "content": "What is the population of Tokyo?"},
                                                                                 # {"role": "assistant", "content": "[Wiki]"},
                                                                                 # {"role": "user", "content": "What is the value of e?"},
                                                                                 # {"role": "assistant", "content": "[Math]"},
                                                                                 # {"role": "user", "content": "What is the meaning of life?"},
                                                                                 # {"role": "assistant", "content": "[QA]"},
                                                                                 # {"role": "user", "content": "What is your favorite color?"},
                                                                                 # {"role": "assistant", "content": "[Human]"},
                                                                                 # {"role": "user", "content": "Can you explain the process of photosynthesis?"},
                                                                                 # {"role": "assistant", "content": "[Wiki]"},
                                                                                 # {"role": "user", "content": "What is the sum of 2+2?"},
                                                                                 # {"role": "assistant", "content": "[Math]"},
                                                                                 # {"role": "user", "content": "What are the symptoms of COVID-19?"},
                                                                                 # {"role": "assistant", "content": "[QA]"},
                                                                                 # {"role": "user", "content": "What is your favorite book?"},
                                                                                 # {"role": "assistant", "content": "[Human]"},
                                                                                 # {"role": "user", "content": "What is the capital of France?"},
                                                                                 # {"role": "assistant", "content": "[Wiki]"},
                                                                                 # {"role": "user", "content": "How can I improve my writing skills?"},
                                                                                 # {"role": "assistant", "content": "[QA]"},
                                                                                 # {"role": "user", "content": "What is the height of Mount Everest?"},
                                                                                 # {"role": "assistant", "content": "[Wiki]"},
                                                                                 # {"role": "user", "content": "What is the value of pi?"},
                                                                                 # {"role": "assistant", "content": "[Math]"},
                                                                                 # {"role": "user", "content": "What is the difference between affect and effect?"},
                                                                                 # {"role": "assistant", "content": "[QA]"},
                                                                                 # {"role": "user", "content": "What is your favorite type of music?"},
                                                                                 # {"role": "assistant", "content": "[Human]"},
                                                                                 # {"role":"user", "content":"What are the coordinates of the two points?"},
                                                                                 # {"role":"assistant", "content":"[Human]"},
                                                                                 {"role": "user", "content": question}], max_tokens=500)
            answer = answer["choices"][0]["message"]["content"]
            question = question + "\n\nOnly answer by [Wiki], [Math], [QA]"
        return answer

class GrammarParser:
    def __init__(self):
        pass

    def parse(self, text):
        try:
            answer = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                messages = [{"role": "system", "content": "You are a model that takes in a text that has a part contained in [ ] and summarizes that part to fit with the rest of the text in order for the paragraph to make sense. "},
                                                            {"role": "user", "content": "My favorite type of cake is [Cheesecake is a sweet dessert consisting of one or more layers. The main, and thickest layer, consists of a mixture of soft, fresh cheese (typically cream cheese or ricotta), eggs, and sugar. If there is a bottom layer, it often consists of a crust or base made from crushed cookies, graham crackers, or pastry. The classic flavor of cheesecake is plain, but it can be flavored or topped with fruit, whipped cream, nuts, cookies, chocolate syrup, or even caramel sauce. Cheesecake can be baked or unbaked (usually refrigerated). Baked cheesecake usually has a firmer texture and a slightly browned top, while unbaked cheesecake is softer and creamier. Cheesecakes are usually served chilled, and they can be stored in the refrigerator for several days.] because it's so rich and creamy."},
                                                            {"role": "assistant", "content": "Answer: My favorite type of cake is cheesecake, a sweet dessert with layers consisting of a mixture of soft, fresh cheese, eggs, and sugar, and often featuring a crust made from crushed cookies or pastry. It can be baked or unbaked, flavored or topped with various ingredients like fruit, whipped cream, or chocolate syrup. It's my favorite because it's so rich and creamy."},
                                                            {"role": "user", "content": "I went on vacation to [Hawaii, a group of volcanic islands located in the central Pacific Ocean. It is the 50th state of the United States and is known for its beautiful beaches, lush tropical forests, and diverse culture. The islands offer a wide range of activities, including surfing, snorkeling, hiking, and exploring historical sites like the Pearl Harbor Memorial. Hawaii's cuisine is a unique blend of flavors from various cultures, including Polynesian, Asian, and American influences.] and had a great time."},
                                                            {"role": "assistant", "content": "Answer: I went on vacation to Hawaii, which is a group of volcanic islands in the central Pacific Ocean known for its beautiful beaches, lush tropical forests, diverse culture, and a range of activities like surfing, snorkeling, hiking, and exploring historical sites. Hawaii also offers a unique cuisine that blends Polynesian, Asian, and American influences and had a great time."},
                                                            {"role": "user", "content": "I love watching movies directed by [Christopher Nolan, an English film director, producer, and screenwriter. He is best known for his mind-bending and nonlinear storytelling, often exploring themes such as identity, time, memory, and the nature of reality. Some of his most popular films include Memento, Inception, the Dark Knight Trilogy, Interstellar, and Tenet. Nolan's films are known for their complex plots and stunning visuals, and they have earned him numerous awards and critical acclaim.] because they are thought-provoking and visually stunning."},
                                                            {"role": "assistant", "content": "Answer: I love watching movies directed by Christopher Nolan, an English film director known for his mind-bending and nonlinear storytelling, which often explores themes like identity, time, memory, and reality. His popular films, such as Memento, Inception, the Dark Knight Trilogy, Interstellar, and Tenet, are characterized by complex plots and stunning visuals, earning him numerous awards and critical acclaim. I enjoy his movies because they are thought-provoking and visually stunning."},
                                                            {"role": "user", "content": text}], max_tokens=500)
        except:
            print("Error: GrammarParser")
        return answer

class AnswerModel:
    def __init__(self):
        pass

    def getAnswer(self, question, type=None):
        try:
            if type == "[Math]":
                return self.mathModel(question)
            elif type == "[QA]":
                return self.qaModel(question)
            elif type == "[Wiki]":
                return self.wikiModel(question)
            elif type == "[Base]":
                return self.base_model_answer(question)
            elif type == "[Human]":
                return self.humanAnswer(question)
            elif type == "[Complete]":
                return self.completeAnswerModel(question)
        except:
            print("Error: AnswerModel")

    def mathModel(self, question):
        return openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[{"role": "system", "content": "You are a assistant which task is to answer questions by using a Calculator tool. The tool can be used by writing [Calculator(equation)] where equation is the equation you want solved."},
                                                      {"role": "user", "content": "Out of 1400 participants, 400 (or 29%) passed the test"},
                                                      {"role": "assistant", "content": "Out of 1400 participants, 400 (or [Calculator(400 / 1400)]%) passed the test."},

                                                      {"role": "user",
                                                       "content": "There are 8 apples and 5 oranges in the fruit basket. What is the total number of fruits in the basket and what percentage do apples represent?"},
                                                      {"role": "assistant",
                                                       "content": "There are 8 apples and 5 oranges in the fruit basket, making a total of [Calculator(8 + 5)] fruits in the basket. Apples represent [Calculator(8 / 13)]% of the total fruits."},

                                                      {"role": "user",
                                                       "content": "Calculate the integral of the function f(x) = x * e^(-x^2) between the limits x = 0 and x = 2."},
                                                      {"role": "assistant",
                                                       "content": "To calculate the integral of the function f(x) = x * e^(-x^2) between the limits x = 0 and x = 2, first find the indefinite integral, F(x): F(x) = [F(x), Calculator(integral(x * e^(-x^2), x))]. Next, evaluate F(x) at the limits x = 0 and x = 2: F(2) - F(0) = [F(2), Calculator(evaluate #F(x)# at x=2)] - [F(0), Calculator(evaluate #F(x)# at x=0)] (approximately)."},

                                                      {"role": "user",
                                                       "content": "Find the derivative of the function f(x) = 1 / (x^2 + 2x + 3) with respect to x evaluated for x = 2."},
                                                      {"role": "assistant",
                                                       "content": "To find the derivative of the function f(x) = 1 / (x^2 + 2x + 3) with respect to x, we can use the chain rule. The derivative, f'(x), is [df(x), Calculator(d(1 / (x^2 + 2x + 3))/dx)]. Next, we evaluate f'(x) at x = 2: f'(2) = [df(2), Calculator(evaluate #df(x)# at x=2)]."},

                                                      {"role": "user",
                                                       "content": "A trapezoid has bases of 6 cm and 10 cm, and a height of 4 cm. Calculate the area of the trapezoid."},
                                                      {"role": "assistant",
                                                       "content": "A trapezoid has bases of 6 cm and 10 cm, and a height of 4 cm. To find the area of the trapezoid, use the formula: A = (1/2) * (b1 + b2) * h. The area of the trapezoid is [Calculator(0.5 * (6 + 10) * 4)] square cm."},

                                                      {"role": "user",
                                                       "content": "The surface area of a cube is 54 square cm. Calculate the length of one side of the cube."},
                                                      {"role": "assistant",
                                                       "content": "The surface area of a cube is 54 square cm. To find the length of one side of the cube, use the formula for the surface area of a cube: A = 6 * s^2. Rearranging the formula and solving for s, we get: s = [Calculator(sqrt(54 / 6))] cm."},

                                                      {"role": "user",
                                                       "content": "A cylinder has a radius of 3 cm and a height of 7 cm. Calculate the volume and surface area of the cylinder."},
                                                      {"role": "assistant",
                                                       "content": "A cylinder has a radius of 3 cm and a height of 7 cm. The volume of the cylinder is [Calculator(3.14159 * 3^2 * 7)] cubic cm (approximately). The surface area of the cylinder is [Calculator(2 * 3.14159 * 3 * (3 + 7))] square cm (approximately)."},

                                                      {"role": "user",
                                                       "content": "A cone has a radius of 4 cm and a height of 6 cm. Calculate the volume and surface area of the cone."},
                                                      {"role": "assistant",
                                                       "content": "A cone has a radius of 4 cm and a height of 6 cm. The volume of the cone is [Calculator((1/3) * 3.14159 * 4^2 * 6)] cubic cm (approximately). The surface area of the cone is [Calculator(3.14159 * 4 * (4 + sqrt(4^2 + 6^2)))] square cm (approximately)."},

                                                      {"role": "user",
                                                       "content": "Find the second derivative of the function f(x) = ln(x^2 + 2x) with respect to x. Evaluate the second derivative to x = 5"},
                                                      {"role": "assistant",
                                                       "content": "To find the second derivative of the function f(x) = ln(x^2 + 2x) with respect to x, first find the first derivative, f'(x), using the chain rule: f'(x) = [df(x), Calculator(d(ln(x^2 + 2x))/dx)]. Next, find the second derivative, f''(x), by differentiating f'(x) with respect to x: f''(x) = [ddf(x), Calculator(d(#df(x)#)/dx)]. Finally we evaluate f''(x) at x = 5: f''(5) = [ddf(5), Calculator(evaluate #ddf(x)# at x=5)]."},

                                                      {"role": "user",
                                                       "content": "Calculate the integral of the function f(x) = x * e^(x^2) between the limits x = 0 and x = 1."},
                                                      {"role": "assistant",
                                                       "content": "To calculate the integral of the function f(x) = x * e^(x^2) between the limits x = 0 and x = 1, first find the indefinite integral, F(x): F(x) = [F(x), Calculator(integral(x * e^(x^2), x))]. Next, evaluate F(x) at the limits x = 0 and x = 1: F(1) - F(0) = [F(1), Calculator(evaluate #F(x)# at x=1)] - [F(0), Calculator(evaluate #F(x)# at x=0)]  (approximately)."},

                                                      {"role": "user",
                                                       "content": "Find the derivative of the function f(x) = (x^2 + 1)^3 with respect to x."},
                                                      {"role": "assistant",
                                                       "content": "To find the derivative of the function f(x) = (x^2 + 1)^3 with respect to x, we can use the chain rule. The derivative, f'(x), is [Calculator(d((x^2 + 1)^3)/dx)]."},

                                                      {"role": "user",
                                                       "content": "Calculate the integral of the function f(x) = (3x^2 - 2x + 1)^2 between the limits x = 0 and x = 2."},
                                                      {"role": "assistant",
                                                       "content": "To calculate the integral of the function f(x) = (3x^2 - 2x + 1)^2 between the limits x = 0 and x = 2, first find the indefinite integral, F(x): F(x) = [F(x), Calculator(integral((3x^2 - 2x + 1)^2))]. Next, evaluate F(x) at the limits x = 0 and x = 2: F(2) - F(0) = [F(2), Calculator(evaluate #F(x)# at x=2)] - [F(0), Calculator(evaluate #F(x)# at x=0)] (approximately)."},

                                                      {"role": "user",
                                                       "content": "Find the derivative of the function f(x) = x^3 * cos(x) with respect to x. Evaluate the derivative at x=2.334"},
                                                      {"role": "assistant",
                                                       "content": "To find the derivative of the function f(x) = x^3 * cos(x) with respect to x, we can use the product rule. The derivative, f'(x), is [df(x), Calculator(d(x^3 * cos(x))/dx)]. Next, we evaluate f'(x) at x=2.334: f'(2.334) = [df(2.334), Calculator(evaluate #df(x)# at x=2.334)]."},

                                                      {"role": "user",
                                                       "content": "Find the derivative of the function f(x) = (2x^3 + 3x^2 - x + 1)^4 with respect to x."},
                                                      {"role": "assistant",
                                                       "content": "To find the derivative of the function f(x) = (2x^3 + 3x^2 - x + 1)^4 with respect to x, we can use the chain rule. The derivative, f'(x), is [Calculator(d((2x^3 + 3x^2 - x + 1)^4)/dx)]."},

                                                      {"role": "user",
                                                       "content": "Calculate the integral of the function f(x) = (3x^2 - 4x + 1)^2 between the limits x = 0 and x = 2."},
                                                      {"role": "assistant",
                                                       "content": "To calculate the integral of the function f(x) = (3x^2 - 4x + 1)^2 between the limits x = 0 and x = 2, first find the indefinite integral, F(x): F(x) = [F(x), Calculator(integral((3x^2 - 4x + 1)^2))]. Next, evaluate F(x) at the limits x = 0 and x = 2: F(2) - F(0) = [F(2), Calculator(evaluate #F(x)# at x=2)] - [F(0), Calculator(evaluate #F(x)# at x=0)] = [Calculator(#F(2)# - #F(0)#)]  (approximately)."},

                                                      {"role": "user",
                                                       "content": "A cone has a height of 9 cm and a base radius of 3 cm. Calculate the volume and the surface area of the cone."},
                                                      {"role": "assistant",
                                                       "content": "A cone has a height of 9 cm and a base radius of 3 cm. The volume of the cone is [Calculator((1/3) * 3.14159 * 3^2 * 9)] cubic cm (approximately). To find the surface area, we first need to calculate the slant height: l = [l, Calculator(sqrt(3^2 + 9^2))] cm (approximately). The surface area of the cone is [Calculator(3.14159 * 3 * (3 + #l#))] square cm (approximately)."},

                                                      {"role": "user",
                                                       "content": "Find the derivative of the function f(x) = (x^2 + 2x + 1) / (x^3 - x + 1) with respect to x. Evaluate the derivative at x=2"},
                                                      {"role": "assistant",
                                                       "content": "To find the derivative of the function f(x) = (x^2 + 2x + 1) / (x^3 - x + 1) with respect to x, we can use the quotient rule. The derivative, f'(x), is [df(x), Calculator(d((x^2 + 2x + 1) / (x^3 - x + 1))/dx)]. Next we evaluate f'(x) at x=2: f'(2) = [df(2), Calculator(evaluate #df(x)# at x=2)]."},

                                                      {"role": "user",
                                                       "content": "A triangle has sides of lengths 5 cm, 7 cm, and 9 cm. Calculate the area of the triangle using Heron's formula."},
                                                      {"role": "assistant",
                                                       "content": "A triangle has sides of lengths 5 cm, 7 cm, and 9 cm. To calculate the area using Heron's formula, first find the semi-perimeter, s: s = [s, Calculator((5 + 7 + 9) / 2)] cm. Next, apply Heron's formula: Area = [Calculator(sqrt(#s# * (#s# - 5) * (#s# - 7) * (#s# - 9)))] square cm (approximately)."},

                                                      {"role": "user",
                                                       "content": "A trapezoid has bases of lengths 6 cm and 8 cm, and a height of 5 cm. Calculate the area of the trapezoid."},
                                                      {"role": "assistant",
                                                       "content": "A trapezoid has bases of lengths 6 cm and 8 cm, and a height of 5 cm. To calculate the area of the trapezoid, use the formula: Area = [Calculator(0.5 * (6 + 8) * 5)] square cm."},

                                                      {"role": "user",
                                                       "content": "An equilateral triangle has a side length of 10 cm. Calculate the height and the area of the triangle."},
                                                      {"role": "assistant",
                                                       "content": "An equilateral triangle has a side length of 10 cm. To calculate the height, use the Pythagorean theorem in a 30-60-90 right triangle formed by bisecting the equilateral triangle: height = [height, Calculator(sqrt(10^2 - (10 / 2)^2))] cm. The area of the triangle is [Calculator(0.5 * 10 * #height#)] square cm."},

                                                      {"role": "user",
                                                       "content": "A car travels 80 km in 1.5 hours. What is the car's average speed in kilometers per hour?"},
                                                      {"role": "assistant",
                                                       "content": "A car travels 80 km in 1.5 hours. To find the car's average speed in kilometers per hour, divide the distance by the time: average speed = [Calculator(80 / 1.5)] km/h."},

                                                      {"role": "user",
                                                       "content": "A rectangle has an area of 60 square cm and a width of 5 cm. Calculate the length of the rectangle."},
                                                      {"role": "assistant",
                                                       "content": "A rectangle has an area of 60 square cm and a width of 5 cm. To find the length of the rectangle, use the formula for the area of a rectangle: Area = length * width. Rearrange the formula and solve for the length: length = [Calculator(60 / 5)] cm."},
                                                      {"role": "user",
                                                       "content": "Find the second derivative of the function f(x) = sin(x) * cos(x) with respect to x. Evaluate the derivative at x=4.6"},
                                                      {"role": "assistant",
                                                       "content": "To find the second derivative of the function f(x) = sin(x) * cos(x) with respect to x, first find the first derivative, f'(x), using the product rule: f'(x) = [df(x), Calculator(d(sin(x) * cos(x))/dx)]. Next, find the second derivative, f''(x), by differentiating f'(x) with respect to x: f''(x) = [ddf(x), Calculator(d(#df(x)#)/dx)]. Next, evaluate f''(x) at x=4.6: f''(4.6) = [ddf(4.6), Calculator(evaluate #ddf(x)# at x=4.6)]."},
                                                      {"role": "user", "content": question}], max_tokens=200)

    def qaModel(self, question):
        return openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[{"role": "system", "content": "you are an assistant who's task is to answer questions using a knowledge base tool capable of answering with verified facts. The tool should help you get information required to complete the text. You can use the tool by writing [QA(question)] where question is the question you want to ask. "},
                                                      # {"role": "user", "content": "What is the Great Wall of China made of?."},
                                                      # {"role": "assistant", "content": "The Great Wall of China is a series of fortifications made of [QA('What materials were used to build the Great Wall of China?')]."},
                                                      # {"role": "user", "content": "What well known tragic story was written by Shakespeare and where is it set?"},
                                                      # {"role": "assistant", "content": "Shakespeare's [x, QA('What is the name of the tragic love story written by Shakespeare?')] is a tragic love story set in [QA('Where is the setting of #x#?')]."},
                                                      {"role": "user", "content": "What is the Eiffel Tower?"},
                                                      {"role": "assistant", "content": "The Eiffel Tower is a [QA('What material is the Eiffel Tower made of?')] tower on the [QA('Where is the Eiffel Tower located in Paris?')] in [QA('In which country is the Eiffel Tower?')]."},
                                                      {"role": "user", "content": "What is the Biggest mountain on earth?"},
                                                      {"role": "assistant", "content": "[x, QA('What is the name of Earth's highest mountain above sea level?')], Earth's highest mountain above sea level, is located in the [QA('In which mountain range is #x# located?')]."},
                                                      # {"role": "user", "content": "What is the main function of the heart?"},
                                                      # {"role": "assistant", "content": "The main function of the heart is to [QA('What is the primary function of the human heart?')], which helps distribute [QA('What substances does the heart help distribute throughout the body?')] throughout the body."},
                                                      # {"role": "user", "content": "What is the primary purpose of the United Nations?"},
                                                      # {"role": "assistant", "content": "The primary purpose of the United Nations is to [QA('What is the main goal of the United Nations?')], which includes promoting [QA('What are some key objectives of the United Nations?')]."},
                                                      # {"role": "user", "content": "What is the capital of Australia?"},
                                                      # {"role": "assistant", "content": "The capital of Australia is [x, QA('What is the capital city of Australia?')], which is located in the [QA('In which territory is #x# located?')]."},
                                                      # {"role": "user", "content": "What is the speed of light?"},
                                                      # {"role": "assistant", "content": "The speed of light is approximately [QA('What is the speed of light in a vacuum in meters per second?')] meters per second in a vacuum."},
                                                      # {"role": "user", "content": "What is the significance of the Mona Lisa?"},
                                                      # {"role": "assistant", "content": "The Mona Lisa is significant because it is a masterpiece by [QA('Who painted the Mona Lisa?')] and is known for its [QA('What are some features that make the Mona Lisa famous?')]."},
                                                      {"role": "user", "content": question}], max_tokens=500)

    def wikiModel(self, question):
        return openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[{"role": "system", "content": "You are a helpfull assistant who's task is to add calls to a wikipedia API to a piece of text. The questions should help you get information required to complete the text. You can call the API by writing [Wiki(subject)] where subject is the subject you want to learn about."},
                                                      {"role": "user", "content": "What is the capital of Germany?"},
                                                      {"role": "assistant", "content": "The capital of Germany is [Wiki(Germany)]."},
                                                      {"role": "user", "content": "Who won the Nobel Prize in Physics in 2021?"},
                                                      {"role": "assistant", "content": "The Nobel Prize in Physics for 2021 was awarded to [Wiki(2021 Nobel Prize in Physics)]."},
                                                      {"role": "user", "content": "What is the tallest mountain in the world?"},
                                                      {"role": "assistant", "content": "The tallest mountain in the world is [Wiki(Mount Everest)]."},
                                                      {"role": "user", "content": "When was the first iPhone released?"},
                                                      {"role": "assistant", "content": "The first iPhone was released in [Wiki(iPhone)]."},
                                                      {"role": "user", "content": "Who is the author of the Harry Potter series?"},
                                                      {"role": "assistant", "content": "The author of the Harry Potter series is [Wiki(J.K. Rowling)]."},
                                                      {"role": "user", "content": "What is the largest mammal on Earth?"},
                                                      {"role": "assistant", "content": "The largest mammal on Earth is the [Wiki(Blue Whale)]."},
                                                      {"role": "user", "content": "What is the distance between the Earth and the Moon?"},
                                                      {"role": "assistant", "content": "The distance between the Earth and the Moon is [Wiki(Earth-Moon distance)]."},
                                                      {"role": "user", "content": "What is the main ingredient in guacamole?"},
                                                      {"role": "assistant",  "content": "The main ingredient in guacamole is [Wiki(Guacamole)]."},
                                                      {"role": "user", "content": "Who was the first person to walk on the Moon?"},
                                                      {"role": "assistant", "content": "The first person to walk on the Moon was [Wiki(Neil Armstrong)]."},
                                                      {"role": "user", "content": "What is the speed of light in a vacuum?"},
                                                      {"role": "assistant", "content": "The speed of light in a vacuum is [Wiki(Speed of Light)]."},
                                                      {"role": "user", "content": "What is the largest planet in our solar system?"},
                                                      {"role": "assistant", "content": "The largest planet in our solar system is [Wiki(Jupiter)]."},
                                                      {"role": "user", "content": "When was the United Nations established?"},
                                                      {"role": "assistant", "content": "The United Nations was established in [Wiki(United Nations)]."},
                                                      {"role": "user", "content": "What is the scientific name for the process of plants converting sunlight into energy?"},
                                                      {"role": "assistant", "content": "The scientific name for the process of plants converting sunlight into energy is [Wiki(Photosynthesis)]."},
                                                      {"role": "user", "content": "What is the smallest country in the world by land area?"},
                                                      {"role": "assistant", "content": "The smallest country in the world by land area is [Wiki(Vatican City)]."},
                                                      {"role": "user", "content": question}], max_tokens=500)

    def completeAnswerModel(self, query):
        answer = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
            {"role": "system",
             "content": "You are a model who answer questions with the use of outside tools. The tools allow to access computing and API of different websites to obtain correct results. These are the tools : [Calculator(equation)], [Wiki(subject)], [QA(question)].\n - The Calculator tool is used to solve numerical equations as well as to resolve complex algebraic equations such as calculus problems.\n- The Wiki tool allows to obtain verified information on a subject.\n- The QA tool is used to answer common knowledge questions questions. \nThe assistant is given a main question as well as subquestions that when answered can help produce a better answer to the main question."},
            {"role": "user",
             "content": "How much force is required to accelerate a 1500 kg car from 0 to 100 km/h in 10 seconds? \n1- How do we convert the velocity from km/h to m/s? \n2- What is the formula to calculate the force required for acceleration? \n3- How do we calculate the force required to accelerate a 1500 kg car from 0 to 100 km/h in 10 seconds?"},
            {"role": "assistant",
             "content": "1- To convert the velocity from km/h to m/s, we can use the following conversion factor: 1 km/h = 1000 m / 3600 s. So, [v_ms, Calculator(100 * (1000/3600))]. \n2- The formula to calculate the force required for acceleration is F = ma, where F is the force, m is the mass, and a is the acceleration. \n3- To calculate the force required to accelerate a 1500 kg car from 0 to 100 km/h in 10 seconds, we first need to find the acceleration. We can use the formula a = Δv / t, where Δv is the change in velocity and t is the time. In this case, Δv is equal to the final velocity in m/s (which we calculated in subquestion 1) minus the initial velocity (0 m/s), and t is 10 seconds. We can then use the formula from subquestion 2 with the mass of the car (1500 kg) and the calculated acceleration to find the force required: \nF = [F, Calculator(1500 * (#v_ms# / 10))]N."},
            {"role": "user",
             "content": "How do you find the integral of the function f(x) = e^(-2x) from 0 to infinity? \n1- What is the antiderivative of e^(-2x)? \n2- How do we evaluate an integral with limits from 0 to infinity? \n3- What is the value of the integral of e^(-2x) from 0 to infinity?"},
            {"role": "assistant",
             "content": "1- To find the antiderivative of e^(-2x), we can use the reverse chain rule. The antiderivative, F(x), is [Calculator(integral(e^(-2x), x))]. \n2- To evaluate an integral with limits from 0 to infinity, we can use the limit concept. We rewrite the integral as the limit of a definite integral with the upper limit t approaching infinity: \nlim (t→∞) ∫[a, t] f(x) dx. \n3- To find the value of the integral of e^(-2x) from 0 to infinity, we can use the antiderivative from subquestion 1 and the limit concept from subquestion 2: \nlim (t→∞) [F(t) - F(0)] = [Calculator((integral(e^(-2x), x, 0, inf))))]."},
            {"role": "user",
             "content": "Can you help me calculate the backpropagation of a small neural network with one hidden layer? Here are the values: \n\nInput layer: x1 = 0.5, x2 = 0.6 \nHidden layer: h1, h2 \nOutput layer: o1 \n\nWeights: \nw1 = 0.1, w2 = 0.2, w3 = 0.3, w4 = 0.4, w5 = 0.5, w6 = 0.6 \n\nActivation function: Sigmoid function \nLoss function: Mean Squared Error (MSE) \n\nTarget output: t1 = 0.8 \n\n1- How do I calculate the forward propagation to find the output value of the network? \n2- How do I calculate the error of the output layer? \n3- How do I update the weights using backpropagation?"},
            {"role": "assistant",
             "content": "1- To calculate the forward propagation, we first need to calculate the weighted sum and activation for the hidden layer neurons and then for the output layer neuron. \n\nFor the hidden layer: \nsum_h1 = w1 * x1 + w2 * x2 \nsum_h2 = w3 * x1 + w4 * x2 \nh1 = sigmoid(sum_h1) \nh2 = sigmoid(sum_h2) \n\nFor the output layer: \nsum_o1 = w5 * h1 + w6 * h2 \no1 = sigmoid(sum_o1) \n\nUsing the given values and sigmoid function: \n[sum_h1, Calculator(0.1 * 0.5 + 0.2 * 0.6)] \n[sum_h2, Calculator( 0.3 * 0.5 + 0.4 * 0.6)] \n[h1, Calculator(1 / (1 + exp(-[sum_h1])))] \n[h2, Calculator(1 / (1 + exp(-sum_h2)))] \n[sum_o1, Calculator(0.5 * h1 + 0.6 * [h2])] \n[o1, Calculator(1 / (1 + exp(-[sum_o1]))')] \n\n2- To calculate the error of the output layer, we'll use the MSE loss function. \n\nE_o1 = 1/2 * (t1 - o1)^2 \n\nUsing the given target output (t1 = 0.8) and calculated output (o1): \n[E_o1, Calculator(1/2 * (0.8 - [o1])^2)] \n\n3- To update the weights using backpropagation, we need to calculate the gradients for each weight and update them accordingly. We'll use the chain rule to find the gradients. \n\nFor weights w5 and w6 (output layer): \ndE_o1_dw5 = dE_o1/do1 * do1/dsum_o1 * dsum_o1/dw5 \ndE_o1_dw6 = dE_o1/do1 * do1/dsum_o1 * dsum_o1/dw6 \n\nFor weights w1, w2, w3, and w4 (hidden layer): \ndE_o1_dw1 = dE_o1/do1 * do1/dsum_o1 * dsum_o1/dh1 * dh1/dsum_h1 * dsum_h1/dw1 \ndE_o1_dw2 = dE_o1/do1 * do1/dsum_o1 * dsum_o1/dh1 * dh1/dsum_h1 * dsum_h1/dw2 \ndE_o1_dw3 = dE_o1/do1 * do1/dsum_o1 * dsum_o1/dh2 * dh2/dsum_h2 * dsum_h2/dw3 \ndE_o1_dw4 = dE_o1/do1 * do1/dsum_o1 * dsum_o1/dh2 * dh2/dsum_h2 * dsum_h2/dw4. Now we need to calculate these gradients using the given values and previously calculated values:\n[dE_o1_do1, Calculator(-(0.8 - [o1]))]\n[do1_dsum_o1, Calculator([o1] * (1 - [o1]))]\n[dsum_o1_dh1, Calculator(0.5)]\n[dsum_o1_dh2, Calculator(0.6)]\n[dh1_dsum_h1, Calculator([h1] * (1 - [h1]))]\n[dh2_dsum_h2, Calculator([h2] * (1 - [h2]))]\n\nNow, we can find the gradients:\n\n[dE_o1_dw5, Calculator([dE_o1_do1] * [do1_dsum_o1] * [dsum_o1_dh1])]\n[Calculator('dE_o1_dw6 = [dE_o1_do1] * [do1_dsum_o1] * [dsum_o1_dh2])]\n[dE_o1_dw1, Calculator([dE_o1_do1] * [do1_dsum_o1] * [dsum_o1_dh1] * [dh1_dsum_h1] * 0.5)]\n[dE_o1_dw2, Calculator([dE_o1_do1] * [do1_dsum_o1] * [dsum_o1_dh1] * [dh1_dsum_h1] * 0.6)]\n[dE_o1_dw3, Calculator([dE_o1_do1] * [do1_dsum_o1] * [dsum_o1_dh2] * [dh2_dsum_h2] * 0.5)]\n[dE_o1_dw4, Calculator([dE_o1_do1] * [do1_dsum_o1] * [dsum_o1_dh2] * [dh2_dsum_h2] * 0.6)]\n\nFinally, we can update the weights using a learning rate(let's say 0.1):\n[w1_updated, Calculator([w1] - 0.1 * [dE_o1_dw1])]\n[w2_updated, Calculator([w2] - 0.1 * [dE_o1_dw2])]\n[w3_updated, Calculator([w3] - 0.1 * [dE_o1_dw3])]\n[w4_updated, Calculator([w4] - 0.1 * [dE_o1_dw4])]\n[w5_updated, Calculator([w5] - 0.1 * [dE_o1_dw5])]\n[w6_updated, Calculator([w6] - 0.1 * [dE_o1_dw6])]\nThese updated weights can then be used for the next iteration of training."},
            {"role": "user", "content": query}], max_tokens=550)

        return answer

    def base_model_answer(self, question):
        return openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "You are a helpfull question answering assistant"},
                                                                             {"role": "user", "content": question}], max_tokens=500)

    def humanAnswer(self, question):
        print(question)
        return input("Answer: ")