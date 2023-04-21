import mysql.connector
from tqdm import tqdm
import time
import pandas as pd

class Database:
    
    def __init__(self, model):
        self.model = model

    def fill_database(self, file_questions:str):

        with open(file_questions, 'r') as f:
            # Load the data from the csv file
            data = pd.read_csv(f, delimiter=';')
            #data = data[100:]

        question_id = 0

        time_start = time.time()
        requests = 0
        tokens = 0
        results = pd.DataFrame(columns=['id', 'question', 'our_model_answer', 'our_model_subquestions', 'our_model_subanswers_bAPI', 'our_model_subanswers_aAPI', 'gpt_answer'])

        for question in tqdm(data["Questions"]):
            answer, sub_questions, answers, API_answers, token, request = self.model.method_complex_tool_answer(question)
            tokens += token
            requests += request
            gpt_answer, token, request = self.model.base_model_answer(question)
            tokens += token
            requests += request
            results = results.append({'id': question_id, 'question': question, 'our_model_answer': answer, 'our_model_subquestions': sub_questions, 'our_model_subanswers_bAPI': answers, 'our_model_subanswers_aAPI':API_answers, 'gpt_answer': gpt_answer}, ignore_index=True)
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
