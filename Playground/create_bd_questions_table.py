import mysql.connector
import json
import tqdm

db = mysql.connector.connect(
    host='localhost',
    user='Antho',
    passwd='Antho1010',
    database='project_database'
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

for sample in tqdm(data):
    try:
        question = sample['question'].replace("'", "''") # replace apostrophes with two apostrophes
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
        
print(f'missing index are the following: ')
for elem in missed_index:
    print(f'-> {elem}')
mycursor.close()
db.close()
