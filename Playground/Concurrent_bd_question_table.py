import mysql.connector
import json
from tqdm import tqdm
from helperGPT import *
import time
import concurrent.futures

db = mysql.connector.connect(
    host='localhost',
    user='Antho',
    passwd='Antho1010',
    database='project_database'
)
mycursor = db.cursor()

# create subquestion table
# mycursor.execute("CREATE TABLE subquestions(question_id INT NOT NULL,subquestion VARCHAR(500) NOT NULL, PRIMARY KEY(question_id, subquestion));")

# Open the JSON file
with open('../hotpot_test_fullwiki_v1.json', 'r') as f:
    # Load the data from the file
    data = json.load(f)

bot = DecompGPT()

def process_question(i):
    question = data[i]['question'].replace("'", "''") # replace apostrophes with two apostrophes
    response_subQ = bot.getSubQuestions(question)
    subquestions = []
    for i in range(len(response_subQ["choices"])):
        subQuestionList = response_subQ["choices"][i]["message"]["content"].split("\n")
        for i, response in enumerate(subQuestionList):
            response = response[3:]
            if '?' in response:
                response = response.replace("'", "''")
                subquestions.append(response)
    return subquestions

# run the getSubQuestion method on 20 threads concurrently
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    results = list(tqdm(executor.map(process_question, range(1232, len(data))), total=len(data)-1232))

# parse the results and add to the SQL database
for i, subquestions in enumerate(results):
    for subquestion in subquestions:
        try:
            string = f"INSERT INTO subquestions (question_id, subquestion) VALUES ({i}, '{subquestion}');"
            mycursor.execute(string)
            db.commit()
        except mysql.connector.Error as error:
            print("Error occurred: {}".format(error))
            print(f'index is : {i} and subquestion is : {subquestion}')

mycursor.close()
db.close()