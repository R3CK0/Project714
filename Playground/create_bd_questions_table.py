import mysql.connector
import json
from tqdm import tqdm
import time

from Playground.helperGPT import QuestionAnswerGPT

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='Answers'
)

mycursor = db.cursor()

# Open the JSON file
with open('../hotpot_test_fullwiki_v1.json', 'r') as f:
    # Load the data from the file
    data = json.load(f)
    # max length question is 274

missed_index = []
question_id = 0
mycursor.execute("CREATE TABLE questions(id INT NOT NULL,question VARCHAR(300) NOT NULL,answer VARCHAR(300) NOT NULL, PRIMARY KEY(id));")

# create timer to make sure there is a maximum of 20 queries per minute
count = 0
time_start = time.time()

model = QuestionAnswerGPT()

for sample in tqdm(data):
    count += 1
    try:
        question = sample['question'].replace("'", "''") # replace apostrophes with two apostrophes
        answer = model.getAnswer()
        string = f"INSERT INTO questions (id, question, answer) VALUES ({question_id}, '{question}', ' ');"
        mycursor.execute(string)
        db.commit()
        question_id += 1
        # mycursor.execute(f"SELECT * FROM questions;")
        # rows = mycursor.fetchall()
        # for row in rows:
        #     print(row)

    except mysql.connector.Error as error:
        print("Error occurred: {}".format(error))
        missed_index.append(question_id)
        question_id += 1

    if count % 20 == 0:
        count = 0
        if time.time()-time_start < 60:
            time.sleep(60-(time.time()-time_start))

        
print(f'missing index are the following: ')
for elem in missed_index:
    print(f'-> {elem}')
mycursor.close()
db.close()
