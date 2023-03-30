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
# mycursor.execute("CREATE TABLE subquestionsDev(question_id INT NOT NULL, question VARCHAR(500) NOT NULL, subquestion VARCHAR(500) NOT NULL, PRIMARY KEY(question_id, subquestion));")

# mycursor.execute(f"SELECT * FROM subquestionsDev WHERE question_id > 6897;")
# rows = mycursor.fetchall()
# for row in rows:
#     print(row)

# Open the JSON file
with open('../database/hotpot_dev_fullwiki_v1.json', 'r') as f:
    # Load the data from the file
    data = json.load(f)

bot = DecompGPT()

for i in tqdm(range(6897, len(data))):
    question = data[i]['question'].replace("'", "''") # replace apostrophes with two apostrophes
    response_subQ = bot.getSubQuestions(question)
    for j in range(len(response_subQ["choices"])):
        subQuestionList = response_subQ["choices"][j]["message"]["content"].split("\n")
        for response in subQuestionList:
            response = response[3:]
            if '?' in response:
                try:
                    response = response.replace("'", "''")
                    string = f"INSERT INTO subquestionsDev (question_id, question, subquestion) VALUES ({i},'{question}' ,'{response}');"
                    mycursor.execute(string)
                    db.commit()

                except mysql.connector.Error as error:
                    print("Error occurred: {}".format(error))
                    print(f'index is : {i} and response is : {response}')
    time.sleep(2)

            
mycursor.close()
db.close()





