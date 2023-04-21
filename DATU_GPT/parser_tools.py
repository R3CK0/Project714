import enum
import re
import wikipediaapi
from api_tools import ToolKit


class Manipulator():

    def __init__(self):
        self.tool = ToolKit()

    def insert_variable(self, var, result):
        self.tool.variables[var] = str(result)

    def replace_keys_with_values(self, s:str):
        for k, v in self.tool.variables.items():
            s = s.replace(f"#{k}#", v)
        return s

    def find_and_extract_all(self, text: str, pattern: str):
        start_index = 0
        indexes = []
        api_calls = []
        variables = []
        token_index = 0
        while token_index != -1:
            token_index = text.find("["+pattern+"(", start_index)
            if token_index == -1:
                token_index = text.find("[", start_index)
                if token_index == -1:
                    break
                else:
                    start_index = token_index + 1
                    variable_index = text.find(", "+pattern+"(", start_index)
                    if variable_index == -1:
                        break
                    variable = text[start_index:variable_index]
                    start_index = variable_index + 3 + len(pattern)
                    call_index = text.find(")]", start_index)
                    api_call = text[start_index:call_index]
                    indexes.append((token_index, call_index+2))
                    api_calls.append(api_call)
                    variables.append(variable)
            else:
                start_index = token_index + 2 + len(pattern)
                call_index = text.find(")]", start_index)
                api_call = text[start_index:call_index]
                indexes.append((token_index, call_index+2))
                api_calls.append(api_call)
                variables.append("unsaved")
        return indexes, api_calls, variables

    def string_replace(self, text, positions, replace):
        add = 0
        for i, response in enumerate(replace):
            text = text[:positions[i][0]+add] + "[" + response + "]" + text[positions[i][1]+add:]
            string_len = len(response)+2
            replace_len = positions[i][1] - positions[i][0]
            add += string_len - replace_len
        return text

    def math_parser(self, text: str):
        indexes, api_calls, variables = self.find_and_extract_all(text, "Calculator")
        results = []
        if len(indexes) > 0:
            for i, call in enumerate(api_calls):
                # replace variables
                call = self.replace_keys_with_values(call)
                if call.startswith('solve'):
                    results.append(self.tool.solve_math_api(call))
                else:
                    results.append(self.tool.call_math_api(call))
                if variables[i] != "unsaved":
                    self.insert_variable(variables[i], results[i])
            text = self.string_replace(text, indexes, results)
        return text

    def qa_parser(self, text: str):
        indexes, api_calls, variables = self.find_and_extract_all(text, "QA")
        results = []
        if len(indexes) > 0:
            for i, call in enumerate(api_calls):
                # replace variables
                call = self.replace_keys_with_values(call)
                results.append(self.tool.call_qa_api(call))
                if variables[i] != "unsaved":
                    self.insert_variable(variables[i], results[i])
            text = self.string_replace(text, indexes, results)
        return text

    def wiki_parser(self, text: str):
        indexes, api_calls, variables = self.find_and_extract_all(text, "Wiki")
        delay = 0
        results = []
        if len(indexes) > 0:
            for i, call in enumerate(api_calls):
                # replace variables
                call = self.replace_keys_with_values(call)
                results.append(self.tool.call_wiki_API(call))
                if variables[i] != "unsaved":
                    self.insert_variable(variables[i], results[i])
            text = self.string_replace(text, indexes, results)
        return text

    def get_content(self, input):
        return input["choices"][0]["message"]["content"], input['usage']['total_tokens']

    def extract_API_call(self, input):
        return self.math_parser(self.wiki_parser(self.qa_parser(input)))


    def reformat_sub_answers(self, answers, grammarModel):
       return [grammarModel.parse(answer) for answer in answers]

    def recomposition_format(self, question, sub_answers):
        sub_answers_concaneted = "\n".join(sub_answers)
        return 'Question: ' + question + '\nFacts: ' + sub_answers_concaneted

    def clear_Toolkit(self):
        self.tool.clear_toolKit()