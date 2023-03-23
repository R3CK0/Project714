import mysql.connector
import json
from tqdm import tqdm
from helperGPT import *
import time

db = mysql.connector.connect(
    host='localhost',
    user='Antho',
    passwd='Antho1010',
    database='project_database'
)
mycursor = db.cursor()

# create subquestion table
# mycursor.execute("CREATE TABLE subquestions(question_id INT NOT NULL,subquestion VARCHAR(500) NOT NULL, PRIMARY KEY(question_id, subquestion));")

# mycursor.execute(f"SELECT * FROM subquestions WHERE question_id > 5000;")
# rows = mycursor.fetchall()
# for row in rows:
#     print(row)

# Open the JSON file
with open('../hotpot_test_fullwiki_v1.json', 'r') as f:
    # Load the data from the file
    data = json.load(f)

bot = DecompGPT()

for i in tqdm(range(5862, len(data))):
    question = data[i]['question'].replace("'", "''") # replace apostrophes with two apostrophes
    response_subQ = bot.getSubQuestions(question)
    for j in range(len(response_subQ["choices"])):
        subQuestionList = response_subQ["choices"][j]["message"]["content"].split("\n")
        for response in subQuestionList:
            response = response[3:]
            if '?' in response:
                try:
                    response = response.replace("'", "''")
                    string = f"INSERT INTO subquestions (question_id, subquestion) VALUES ({i}, '{response}');"
                    mycursor.execute(string)
                    db.commit()

                except mysql.connector.Error as error:
                    print("Error occurred: {}".format(error))
                    print(f'index is : {i} and response is : {response}')
    time.sleep(2)

            
mycursor.close()
db.close()





