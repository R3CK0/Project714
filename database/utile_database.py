import mysql.connector
import json
from concurrent.futures import ThreadPoolExecutor
from helperGPT import DecompGPT
from tqdm import tqdm
import time

db = mysql.connector.connect(
    host='localhost',
    user='Antho',
    passwd='Antho1010',
    database='project_database'
)

cursor = db.cursor()

cursor.execute(f"SELECT * FROM questionsanswers JOIN subquestions ON questionsanswers.id = subquestions.question_id;")
rows = cursor.fetchall()

print(f'the number of element is: {len(rows)}')
print(f'the last element is: {rows[-1]}')

# usefull to get rows
# cursor.execute(f"SELECT * FROM questionsanswers;")
# rows = cursor.fetchall()
# print('questionsanswers database')
# print(f'the number of question is: {len(rows)}')
# print(f'the last id value is : {rows[-1]}')


# close database connection
cursor.close()
db.close()
