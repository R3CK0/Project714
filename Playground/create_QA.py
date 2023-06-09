import mysql.connector
import json
import time
from tqdm import tqdm
from helperGPT import QuestionAnswerGPT

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='N1c0o9a5$',
    database='mydatabases'

)

mycursor = db.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")
# mycursor.execute("CREATE TABLE questions (id INT PRIMARY KEY, question VARCHAR(300), answer VARCHAR("
#                    "2000))")
#
# mySql_insert_query = """INSERT INTO questions (id, question, answer)
#                        VALUES
#                        (1, 'which laptop do you have ?', 'Lenovo ThinkPad E470') """
#
#
# mycursor.execute(mySql_insert_query)
# db.commit()
# print(mycursor.rowcount, "Record inserted successfully into Laptop table")
# mycursor.close()


# string1 = f"select * from questions ORDER BY id DESC LIMIT 1;"
# mycursor.execute(string1)
# db.commit()


# Open the JSON file
with open('../database/hotpot_dev_fullwiki_v1.json', 'r') as f:
    # Load the data from the file
    data = json.load(f)
    # max length question is 274

missed_index = []



# question = data[0]['question']
model = QuestionAnswerGPT()
"""

"""
# # create timer to make sure there is a maximum of 20 queries per minute
count = 0
time_start = time.time()
question_id = 5644
questions = list(data)



for sample in tqdm(questions[5644:], desc = 'Answering Questions'):
   #print(f'question id is {question_id}')
   count += 1
   try:
        question = sample['question'].replace("\"", "'")
        answer = model.getAnswer(question)['choices'][0]['message']['content']
        answer = answer.replace("\"", "'")

        string = f"INSERT INTO devset (id, question , answer) VALUES (\"{question_id}\" , \"{question}\" , \"{answer}\" );"
        question_id +=1
        mycursor.execute(string)
        db.commit()


   except mysql.connector.Error as error:
         print("Error occurred: {}".format(error))
         missed_index.append(question_id)
         question_id += 1

   if count % 20 == 0:
       count = 0
       if time.time() - time_start < 70:
           time.sleep(70 - (time.time() - time_start))
           time_start = time.time()
