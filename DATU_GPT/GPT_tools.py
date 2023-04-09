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

class GrammarParser:
    def __init__(self):
        self.API_KEY = open("../../OpenAIApproach/OpenAIAPIKey.txt", "r").read()
        openai.api_key = self.API_KEY

    def parse(self, text):
        return openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages = [{"role": "system", "content": "You are a model that takes in a text that has a part contained in [ ] and summarizes that part to fit with the rest of the text in order for the paragraph to make sense. "},
                                                        {"role": "user", "content": "My favorite type of cake is [Cheesecake is a sweet dessert consisting of one or more layers. The main, and thickest layer, consists of a mixture of soft, fresh cheese (typically cream cheese or ricotta), eggs, and sugar. If there is a bottom layer, it often consists of a crust or base made from crushed cookies, graham crackers, or pastry. The classic flavor of cheesecake is plain, but it can be flavored or topped with fruit, whipped cream, nuts, cookies, chocolate syrup, or even caramel sauce. Cheesecake can be baked or unbaked (usually refrigerated). Baked cheesecake usually has a firmer texture and a slightly browned top, while unbaked cheesecake is softer and creamier. Cheesecakes are usually served chilled, and they can be stored in the refrigerator for several days.] because it's so rich and creamy."},
                                                        {"role": "assistant", "content": "Answer: My favorite type of cake is cheesecake, a sweet dessert with layers consisting of a mixture of soft, fresh cheese, eggs, and sugar, and often featuring a crust made from crushed cookies or pastry. It can be baked or unbaked, flavored or topped with various ingredients like fruit, whipped cream, or chocolate syrup. It's my favorite because it's so rich and creamy."},
                                                        {"role": "user", "content": "I went on vacation to [Hawaii, a group of volcanic islands located in the central Pacific Ocean. It is the 50th state of the United States and is known for its beautiful beaches, lush tropical forests, and diverse culture. The islands offer a wide range of activities, including surfing, snorkeling, hiking, and exploring historical sites like the Pearl Harbor Memorial. Hawaii's cuisine is a unique blend of flavors from various cultures, including Polynesian, Asian, and American influences.] and had a great time."},
                                                        {"role": "assistant", "content": "Answer: I went on vacation to Hawaii, which is a group of volcanic islands in the central Pacific Ocean known for its beautiful beaches, lush tropical forests, diverse culture, and a range of activities like surfing, snorkeling, hiking, and exploring historical sites. Hawaii also offers a unique cuisine that blends Polynesian, Asian, and American influences and had a great time."},
                                                        {"role": "user", "content": "I love watching movies directed by [Christopher Nolan, an English film director, producer, and screenwriter. He is best known for his mind-bending and nonlinear storytelling, often exploring themes such as identity, time, memory, and the nature of reality. Some of his most popular films include Memento, Inception, the Dark Knight Trilogy, Interstellar, and Tenet. Nolan's films are known for their complex plots and stunning visuals, and they have earned him numerous awards and critical acclaim.] because they are thought-provoking and visually stunning."},
                                                        {"role": "assistant", "content": "Answer: I love watching movies directed by Christopher Nolan, an English film director known for his mind-bending and nonlinear storytelling, which often explores themes like identity, time, memory, and reality. His popular films, such as Memento, Inception, the Dark Knight Trilogy, Interstellar, and Tenet, are characterized by complex plots and stunning visuals, earning him numerous awards and critical acclaim. I enjoy his movies because they are thought-provoking and visually stunning."},
                                                        {"role": "user", "content": text}], max_tokens=500)

class AnswerModel:
    def __init__(self):
        self.API_KEY = open("../../OpenAIApproach/OpenAIAPIKey.txt", "r").read()
        openai.api_key = self.API_KEY

    def getAnswer(self, question, type):
        if type == "[Math]":
            return self.mathModel(question)
        elif type == "[QA]":
            return self.qaModel(question)
        elif type == "[Wiki]":
            return self.wikiModel(question)
        elif type == "[Human]":
            return self.humanAnswer(question)

    def mathModel(self, question):
        return openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[{"role": "system", "content": "You are a assistant which task is to add calls to a Calculator API to a piece of text related to a math problem. The calculations should help you get information required to complete the text. You can call the API by writing [Calculator(equation)] where equation is the equation you want solved."},
                                                      {"role": "user", "content": "There are 8 apples and 5 oranges in the fruit basket. What is the total number of fruits in the basket and what percentage do apples represent?"},
                                                      {"role": "assistant", "content": "There are 8 apples and 5 oranges in the fruit basket, making a total of [Calculator(8 + 5)] fruits in the basket. Apples represent [Calculator(8 / 13)]% of the total fruits."},
                                                      {"role": "user", "content": "A car travels 120 miles in 3 hours. What is the average speed of the car in miles per hour?"},
                                                      {"role": "assistant", "content": "A car travels 120 miles in 3 hours. The average speed of the car is [Calculator(120 / 3)] miles per hour."},
                                                      {"role": "user", "content": "If a shirt costs $25 and there is a 15% discount, what is the final price of the shirt?"},
                                                      {"role": "assistant", "content": "If a shirt costs $25 and there is a 15% discount, the discount amount is $[Calculator(25 * 0.15)]. The final price of the shirt is $[Calculator(25 - 3.75)]."},
                                                      {"role": "user", "content": "A rectangle has a length of 12 cm and a width of 8 cm. What is the area and the perimeter of the rectangle?"},
                                                      {"role": "assistant", "content": "A rectangle has a length of 12 cm and a width of 8 cm. The area of the rectangle is [Calculator(12 * 8)] square cm. The perimeter of the rectangle is [Calculator(2 * (12 + 8))] cm."},
                                                      {"role": "user", "content": "If a cyclist covers a distance of 36 km in 2 hours, what is their average speed in kilometers per hour?"},
                                                      {"role": "assistant", "content": "If a cyclist covers a distance of 36 km in 2 hours, their average speed is [Calculator(36 / 2)] kilometers per hour."},
                                                      {"role": "user", "content": "A triangle has a base of 14 cm and a height of 6 cm. What is the area of the triangle?"},
                                                      {"role": "assistant", "content": "A triangle has a base of 14 cm and a height of 6 cm. The area of the triangle is [Calculator(0.5 * 14 * 6)] square cm."},
                                                      {"role": "user", "content": "A circle has a radius of 5 cm. Calculate the circumference and the area of the circle."},
                                                      {"role": "assistant", "content": "A circle has a radius of 5 cm. The circumference of the circle is [Calculator(2 * 3.14159 * 5)] cm (approximately). The area of the circle is [Calculator(3.14159 * 5^2)] square cm (approximately)."},
                                                      {"role": "user", "content": "A sphere has a volume of 288 cubic cm. Calculate the radius of the sphere."},
                                                      {"role": "assistant", "content": "A sphere has a volume of 288 cubic cm. To find the radius, we use the formula for the volume of a sphere: V = (4/3) * π * r^3. Rearranging the formula and solving for r, we get: r = [Calculator(((3 * 288) / (4 * 3.14159))^(1/3))] cm (approximately)." },
                                                      {"role": "user", "content": "A rectangular prism has a length of 10 cm, a width of 6 cm, and a height of 4 cm. Calculate the volume and surface area of the prism."},
                                                      {"role": "assistant", "content": "A rectangular prism has a length of 10 cm, a width of 6 cm, and a height of 4 cm. The volume of the prism is [Calculator(10 * 6 * 4)] cubic cm. The surface area of the prism is [Calculator(2 * (10 * 6 + 10 * 4 + 6 * 4))] square cm."},
                                                      {"role": "user", "content": question}], max_tokens=1000)

    def qaModel(self, question):
        return openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[{"role": "system", "content": "you are an assistant who's task is to add calls to a Question Answering API to a piece of text. The questions should help you get information required to complete the text. You can call the API by writing [QA(question)] where question is the question you want to ask. "},
                                                      {"role": "user", "content": "What is the Great Wall of China made of?."},
                                                      {"role": "assistant", "content": "The Great Wall of China is a series of fortifications made of [QA('What materials were used to build the Great Wall of China?')]."},
                                                      {"role": "user", "content": "What well known tragic story was written by Shakespeare and where is it set?"},
                                                      {"role": "assistant", "content": "Shakespeare's [x, QA('What is the name of the tragic love story written by Shakespeare?')] is a tragic love story set in [QA('Where is the setting of [x]?')]."},
                                                      {"role": "user", "content": "What is the Eiffel Tower?"},
                                                      {"role": "assistant", "content": "The Eiffel Tower is a [QA('What material is the Eiffel Tower made of?')] tower on the [QA('Where is the Eiffel Tower located in Paris?')] in [QA('In which country is the Eiffel Tower?')]."},
                                                      {"role": "user", "content": "What is the Biggest mountain on earth?"},
                                                      {"role": "assistant", "content": "[x, QA('What is the name of Earth's highest mountain above sea level?')], Earth's highest mountain above sea level, is located in the [QA('In which mountain range is [x] located?')]."},
                                                      {"role": "user", "content": "What is the main function of the heart?"},
                                                      {"role": "assistant", "content": "The main function of the heart is to [QA('What is the primary function of the human heart?')], which helps distribute [QA('What substances does the heart help distribute throughout the body?')] throughout the body."},
                                                      {"role": "user", "content": "What is the primary purpose of the United Nations?"},
                                                      {"role": "assistant", "content": "The primary purpose of the United Nations is to [QA('What is the main goal of the United Nations?')], which includes promoting [QA('What are some key objectives of the United Nations?')]."},
                                                      {"role": "user", "content": "What is the capital of Australia?"},
                                                      {"role": "assistant", "content": "The capital of Australia is [x, QA('What is the capital city of Australia?')], which is located in the [QA('In which territory is [x] located?')]."},
                                                      {"role": "user", "content": "What is the speed of light?"},
                                                      {"role": "assistant", "content": "The speed of light is approximately [QA('What is the speed of light in a vacuum in meters per second?')] meters per second in a vacuum."},
                                                      {"role": "user", "content": "What is the significance of the Mona Lisa?"},
                                                      {"role": "assistant", "content": "The Mona Lisa is significant because it is a masterpiece by [QA('Who painted the Mona Lisa?')] and is known for its [QA('What are some features that make the Mona Lisa famous?')]."},
                                                      {"role": "user", "content": question}], max_tokens=1200)

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
                                                      {"role": "user", "content": question}], max_tokens=750)

    def humanAnswer(self, question):
        print(question)
        return input("Answer: ")