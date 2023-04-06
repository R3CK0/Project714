import enum
import re
import requests

#TODO
# model classifier

# model reformating answer

class ModelType(enum.Enum):
    math = 'math'
    wiki = 'wiki'
    

def call_wiki_API(search:str):
    # Define the base URL of the Wikipedia API
    WIKIPEDIA_API_URL = "https://en.wikipedia.org/w/api.php"

    # Define the search parameters
    search_params = {
        "action": "query",
        "list": "search",
        "srsearch": search,
        "format": "json"
    }

    # Send the HTTP GET request to the API and get the JSON response
    response = requests.get(WIKIPEDIA_API_URL, params=search_params)
    response_json = response.json()

    # Extract the search results from the JSON response
    search_results = response_json["query"]["search"]

    # Print the title and snippet of each search result
    # for result in search_results:
    #     print(f"Title: {result['title']}")
    #     print(f"Snippet: {result['snippet']}")
    #     print("=" * 50)
    return search_results

def remove_pattern(text: str, pattern: str) -> tuple:
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
    
def find_and_extract_all(text:str, pattern:str):
    indexes = []
    remove_patterns = []
    new_text, index, removed_pattern = remove_pattern(text, pattern)
    while(index != -1):
        indexes.append(index)
        remove_patterns.append(removed_pattern)
        new_text, index, removed_pattern = remove_pattern(new_text, pattern)
    return indexes, remove_patterns

def insert_string(original_str, insert_str, pos):
    return original_str[:pos] + insert_str + original_str[pos:]

def parse_math(text:str):
    indexes, paterns_removed = find_and_extract_all(text, '^\[calculate<[0-9a-zA-Z\p{Sm}]*>\]$')
    for i in range(len(paterns_removed)):
        patern_removed = patern_removed[12:-2]
        try:
            result = eval(patern_removed)
            text = insert_string(text, result, indexes[i])
        except NameError as e:
            print(str(e))
    return text

def parse_wiki(input:str):
    # find pattern remove and keep index start
    for i in range(len(paterns_removed)):
        indexes, paterns_removed = find_and_extract_all(text, '\[wiki<.*?>\]')
        patern_removed = patern_removed[7:-2]
        try:
            # call wiki api
            result = call_wiki_API(patern_removed)
            text = insert_string(text, result, indexes[i])
        except NameError as e:
            print(str(e))
    return text

def parse_answer(input:str, model_type):
    if(model_type == ModelType.math):
        answer = parse_math(input)
    elif(model_type == ModelType.wiki):
        answer = parse_wiki()
    else:
        print(f'There was an error, no model type {model_type} exist...')
    return answer
