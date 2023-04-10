import enum
import regex as re
import wikipediaapi
from api_tools import ToolKit


class Manipulator():

    def __init__(self):
        tool = ToolKit()
        pass

    class ModelType(enum.Enum):
        math = 'math'
        wiki = 'wiki'
        
    def format_and_insert_var(self, var, result):
        var = var.replace(",", "").replace("[", "").replace("]", "").replace(" ", "").replace("(", "").replace(")", "")
        self.tool.variables[var] = str(result)

    def replace_keys_with_values(self, s:str):
        for k, v in self.tool.variables.items():
            s = s.replace(f"#{k}#", v)
        return s

    def remove_pattern(self, text: str, pattern: str) -> tuple:
        # Compile the regex pattern
        regex_pattern = re.compile(pattern)
        # Search for the pattern in the text
        match = regex_pattern.search(text)
        if match:
            # Get the start index and end index of the match
            start_index = match.start()
            end_index = match.end()
            # Remove the match from the text and save it as removed_pattern
            text_before = text[:start_index]
            text_after = text[end_index:]
            removed_pattern = match.group(0)
            text = text_before + text_after
        else:
            start_index = -1
            removed_pattern = ""
        return text, start_index, removed_pattern

    def find_and_extract_all(self, text: str, pattern: str):
        indexes = []
        remove_patterns = []
        new_text, index, removed_pattern = self.remove_pattern(text, pattern)
        while index != -1:
            indexes.append(index)
            remove_patterns.append(removed_pattern)
            new_text, index, removed_pattern = self.remove_pattern(new_text, pattern)
        return indexes, remove_patterns

    def insert_string(self, original_str, insert_str, pos):
        return original_str[:pos] + '[' + insert_str + ']' + original_str[pos:]

    def parse_math(self, text: str):
        indexes, patterns_removed = self.find_and_extract_all(text, '^\[[a-zA-Z0-9_-,()]*Calculator([0-9a-zA-Z#\p{Sm}]*)\]$')
        for i in range(len(patterns_removed)):
            split_pattern = patterns_removed[i].split('Calculator(')
            expression = split_pattern[-1][:-2]
            # replace variables
            expression = self.replace_keys_with_values(expression)
            try:
                if expression.startswith('solve'):
                    result = self.tool.solve_math_api(expression)
                else:
                    result = self.tool.call_math_api(expression)
                
                text = self.insert_string(text, result, indexes[i])
                if len(split_pattern) > 1:
                    # adding variables to dictionary
                    self.format_and_insert_var(split_pattern[0], result)
            except NameError as e:
                print(str(e))
        return text

    def parse_wiki(self, text: str):
        # find pattern remove and keep index start
        indexes, paterns_removed = self.find_and_extract_all(text, '\[Wiki(.*?)\]')
        for i in range(len(paterns_removed)):
            patern_removed = patern_removed[7:-2]
            try:
                # call wiki api
                result = self.tool.call_wiki_API(patern_removed)
                text = self.insert_string(text, result, indexes[i])
            except NameError as e:
                print(str(e))
        return text

    def parse_qa(self, text: str):
        # find patten remove and keep index start
        indexes, paterns_removed = self.find_and_extract_all(text, '\[[a-zA-Z0-9_-,()]*QA(.*?)\]')
        for i in range(len(paterns_removed)):
            split_pattern = paterns_removed[i].split('QA(')
            patern_removed = split_pattern[-1][:-2]
            #patern_removed = patern_removed[5:-2]
            try:
                # call qa api
                result = self.tool.call_qa_API(patern_removed)
                text = self.insert_string(text, result, indexes[i])
                if len(split_pattern) > 1:
                    if len(split_pattern) > 1:
                        self.format_and_insert_var(split_pattern[0], result)
            except NameError as e:
                print(str(e))
        return text

    def get_content(self, input):
        return input["choices"][0]["message"]["content"]

    def extract_API_call(self, input):
        return self.parse_math(self.parse_wiki(self.parse_qa(input)))

    def reformat_sub_answers(self, answers, grammarModel):
       return [grammarModel.parse(answer) for answer in answers]

    def recomposition_format(self, question, sub_answers):
        sub_answers_concaneted = "\n".join(sub_answers)
        return 'Question: ' + question + '\nFacts: ' + sub_answers_concaneted
        