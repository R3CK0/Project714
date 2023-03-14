import mysql.connector
import json
import time
from tqdm import tqdm
#from helperGPT import *

from Playground.helperGPT import QuestionAnswerGPT

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='answers'
)

mycursor = db.cursor()

# Open the JSON file
with open('../hotpot_test_fullwiki_v1.json', 'r') as f:
    # Load the data from the file
    data = json.load(f)
    # max length question is 274

missed_index = []
question_id = 0

question = data[0]['question']
model = QuestionAnswerGPT()
answer = model.getAnswer(question)
print (answer['choices'][0]['message']['content'])

for sample in tqdm(data):

   try:

       question = sample['question'].replace("'", "''")
       answer = model.getAnswer(question)['choices'][0]['message']['content']
       string = f"INSERT INTO questions (id, question ,answer) VALUES ({question_id}, '{question}', '{answer}');"
       mycursor.execute(string)
       db.commit()
       question_id +=1
       time.sleep(3)

   except mysql.connector.Error as error:
         print("Error occurred: {}".format(error))
         missed_index.append(question_id)
         question_id += 1

print(f'missing index are the following: ')
for elem in missed_index:
    print(f'-> {elem}')


mycursor.close()
db.close()
