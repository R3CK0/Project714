import mysql.connector
from tqdm import tqdm
import time
import pandas as pd

class Database:
    
    def __init__(self, model):
        # self.db = mysql.connector.connect(
        #     host='localhost',
        #     user='root',
        #     passwd='N1c0o9a5$',
        #     database='Answers'
        # )
        # self.mycursor = self.db.cursor()
        self.model = model

        
    # def create_table(self):
    #     self.mycursor.execute("CREATE TABLE decomp_recomp_model (id INT NOT NULL,question VARCHAR(300) NOT NULL,our_model_answer VARCHAR(300) NOT NULL, our_model_reasoning VARCHAR(300) NOT NULL, our_model_facts VARCHAR(300) NOT NULL, gpt_answer VARCHAR(300) NOT NULL, PRIMARY KEY(id));")
    #
    def fill_database(self, file_questions:str):

        # Open the JSON file
        with open(file_questions, 'r') as f:
            # Load the data from the csv file
            data = pd.read_csv(f, delimiter=';')
            data = data[78:]
            # max length question is 274

        missed_index = []
        question_id = 0
 
        # create timer to make sure there is a maximum of 20 queries per minute
        time_start = time.time()
        requests = 0
        tokens = 0
        results = pd.DataFrame(columns=['id', 'question', 'our_model_answer_bAPI', 'our_model_answer_aAPI', 'gpt_answer'])

        for question in tqdm(data["Questions"]):
            answer, API_answer, token, request = self.model.method_data_qa_tool_answer(question)
            tokens += token
            requests += request
            gpt_answer, token, request = self.model.base_model_answer(question)
            tokens += token
            requests += request
            results = results.append({'id': question_id, 'question': question, 'our_model_answer_bAPI': answer, 'our_model_answer_aAPI': API_answer, 'gpt_answer': gpt_answer}, ignore_index=True)
            #string = f"INSERT INTO questions_answer_model (id, question, our_model_answer, our_model_reasoning, our_model_facts, gpt_answer) VALUES ({question_id}, '{question}', '{answer}', '{reasoning}', '{facts}', '{gpt_answer}');"
            #self.mycursor.execute(string)
            #self.db.commit()
            question_id += 1
            results.to_csv('results.csv', index=False)

            if requests >= 58:
                if time.time()-time_start < 60:
                    print(f"reached max requests, sleeping for {60 - (time.time() - time_start)} seconds")
                    time.sleep(60-(time.time()-time_start))
                    requests = 0
                    tokens = 0

            if tokens >= 56000:
                if time.time()-time_start < 60:
                    print(f"reached max tokens, sleeping for {60 - (time.time() - time_start)} seconds")
                    time.sleep(60-(time.time()-time_start))
                    requests = 0
                    tokens = 0

            if time.time()-time_start >= 60:
                requests = 0
                tokens = 0
            
            
    # def __del__(self):
    #     self.mycursor.close()
    #     self.db.close()
