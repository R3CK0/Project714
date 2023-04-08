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