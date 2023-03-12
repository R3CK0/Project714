import openai
import ujson

API_KEY = open("../OpenAIAPIKey.txt", "r").read()

openai.api_key = API_KEY

main_question = "What is there about American society that makes baseball America's national pastime?"
response_subQ = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "You are a helpful assistant that suggests sub-questions to help to answer a more complicated Question"},
                                                                             {"role": "user", "content": "If I throw a baseball how far will it go?"},
                                                                             {"role": "assistant", "content": "1- How much force was placed into the throw? \n2- Are you in an open space? \n3- What angle did you throw the ball in?"},
                                                                             {"role": "user", "content": "If I kick this ball what will happen?"},
                                                                             {"role": "assistant", "content": "1- How hard are you going to kick the ball?\n2- What kind of surface are you kicking it on?\n3- Is the ball inflated properly?\n4- What kind of ball is it?\n5- Will someone be there to catch it or will it hit a wall or the ground?"},
                                                                             {"role": "user", "content": "Were Scott Derrickson and Ed Wood of the same nationality?"},
                                                                             {"role": "assistant", "content": "1- What nationality is Scott Derrickson? \n2- What nationality is Ed Wood?"},
                                                                             {"role": "user", "content": "What is Hierarchical Task Network"},
                                                                             {"role": "assistant", "content": "1- What are the main components of a Hierarchical Task Network? \n2- How is a Hierarchical Task Network used in artificial intelligence? \n3- What are the advantages of using a Hierarchical Task Network approach versus other methods? \n4- Can you provide an example scenario of how a Hierarchical Task Network might be used in practice?"},
                                                                             {"role": "user", "content": main_question}], max_tokens=750)


subQuestionList = response_subQ["choices"][0]["message"]["content"].split("\n")

# response_chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "You are a helpful assistant that asks questions in a given subject"},
#                                                                              {"role": "user", "content": "Physics"},
#                                                                              {"role": "assistant", "content": "1- What is the mass of the sun? \n2- How much force is needed to lift a 100kg object? \n3- What is the speed of light?"},
#                                                                              {"role": "user", "content": "Medecine"},
#                                                                              {"role": "assistant", "content": "1- How do you perform an apendectemy? \n2- What part of the body is the colon found in? \n3- What is the average lifespan of a human being"},
#                                                                              {"role": "user", "content": "Gastrointestinal Medecine"} ], max_tokens=750)

subanswerList = []
for question in subQuestionList:
    question = question + "\n".join(subanswerList)
    responseQA = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "You are a helpful assistant that answers questions"},
                                                                              {"role": "user", "content": question}], max_tokens=500)
    subanswerList.append(responseQA["choices"][0]["message"]["content"])

context = "\n".join(subanswerList)
recompQuestion = "Main Question: " + main_question + context
responseRecomp = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=[{"role": "system", "content": "You are a question answering assistant that uses context to answer a main question as well as provide justification using the contex"},
                                                                         {"role": "user", "content": "Main Question: Were Scott Derrickson and Ed Wood of the same nationality? \nScott Derrickson was born in 1986 in New York, USA\nEd wood was born in 1924 in Ohio, USA"},
                                                                         {"role": "assistant", "content": "Yes, they were both born in the USA\nScott Derrickson was born in the USA and Ed wood was born in the USA. Since they where both born in the same nation they share nationnality"},
                                                                         {"role": "user", "content": recompQuestion}], max_tokens=500)

classic_response = responseQA = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "You are a helpful assistant that answers questions"},
                                                                              {"role": "user", "content": main_question}], max_tokens=500)

print("Main Question: " + main_question)
print("\nSubquestions Generated: " + response_subQ["choices"][0]["message"]["content"])
print("\nSubanswers Generated: " + context)
print("\nFinal answer: " + responseRecomp["choices"][0]["message"]["content"])
print("\nClassic answer: " + classic_response["choices"][0]["message"]["content"])