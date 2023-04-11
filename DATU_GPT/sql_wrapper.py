import mysql.connector
import csv
from tqdm import tqdm
import time
from DATU import *

class Database:
    
    def __init__(self):
        self.db = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='N1c0o9a5$',
            database='Answers'
        )
        self.mycursor = self.db.cursor()

        
    def create_table(self):
        self.mycursor.execute("CREATE TABLE decomp_recomp_model (id INT NOT NULL,question VARCHAR(300) NOT NULL,our_model_answer VARCHAR(300) NOT NULL, our_model_reasoning VARCHAR(300) NOT NULL, our_model_facts VARCHAR(300) NOT NULL, gpt_answer VARCHAR(300) NOT NULL, PRIMARY KEY(id));")
        
    def fill_database(self, file_questions:str):

        # Open the JSON file
        with open(file_questions, 'r') as f:
            # Load the data from the csv file
            data = csv.reader(f)
            # max length question is 274

        missed_index = []
        question_id = 0
 
        # create timer to make sure there is a maximum of 20 queries per minute
        count = 0
        time_start = time.time()

        for question in tqdm(data):
            count += 1
            try:
                answer, reasoning, facts = self.model.method_decomp_answer(question)
                gpt_answer = self.model.base_model_answer(question)
                string = f"INSERT INTO questions_answer_model (id, question, our_model_answer, our_model_reasoning, our_model_facts, gpt_answer) VALUES ({question_id}, '{question}', '{answer}', '{reasoning}', '{facts}', '{gpt_answer}');"
                self.mycursor.execute(string)
                self.db.commit()
                question_id += 1

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
            
            
    def __del__(self):
        self.mycursor.close()
        self.db.close()
