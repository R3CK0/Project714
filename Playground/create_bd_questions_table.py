import mysql.connector
import json
import tqdm


# db = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     passwd='root',
#     database='Answers'
# )
#
# mycursor = db.cursor()

# Open the JSON file
with open('../hotpot_dev_fullwiki_v1.json', 'r') as f:
    # Load the data from the file
    data = json.load(f)
    # max length question is 274

print(len(data))

""" 
missed_index = []
question_id = 0
mycursor.execute("CREATE TABLE Answer(id INT NOT NULL,answer VARCHAR(3000) NOT NULL,answer VARCHAR(3000) NOT NULL, PRIMARY KEY(id));")

model = QuestionAnswerGPT()

for sample in tqdm(data):
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
        
print(f'missing index are the following: ')
for elem in missed_index:
    print(f'-> {elem}')
mycursor.close()
db.close()
"""