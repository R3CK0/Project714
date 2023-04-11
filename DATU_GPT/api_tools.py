import wikipediaapi
import urllib.parse
import requests
from serpapi import GoogleSearch
import sympy as sp

class ToolKit():
    def __init__(self):
        self.variables = {}
        pass
    
    def url_encode(self, string):
        return urllib.parse.quote_plus(string)

    def make_request(self, url, params):
        response = requests.get(url, params=params)
        if response.status_code == 200:
            try:
                return response.content.decode('utf-8')
            except UnicodeDecodeError:
                return response.content.decode('ISO-8859-1')
        else:
            return None

    def call_wiki_API(self, query: str):
        wiki_wiki = wikipediaapi.Wikipedia('en')
        search_results = wiki_wiki.search(query)
        page = wiki_wiki.page(search_results[0])
        return page.summary

    # TODO : Complete qa API and improve math API
    def call_qa_api(self, query: str):
        # print("QA API not implemented yet")

        params = {
            "q": query,
            "location": "Austin, Texas, United States",
            "hl": "en",
            "gl": "us",
            "google_domain": "google.com",
            "api_key": "d3c1e5fa3b313bdea475bb3364f9fa9b5adc719cf26b26afd7502e7eef728e5e"
        }

        search = GoogleSearch(params)

        results = search.get_dict()
        result = results['answer_box']['snippet_highlighted_words']
        res = ''.join(result)
        return res
        # return input(query + " : ")
        # return "replace this part using you best judgement"

    

    # def call_math_api(self, query: str):
    #     print("\n=================Calling math API=================")
    #     print(query)
    #     params = {"appid": '74UV94-Q95PR46UGT', "i": query, "format": "MathematicaInput"}
    #     result = self.make_request("http://api.wolframalpha.com/v2/result", params)
    #     if result is None:
    #         result = "Error: Invalid expression"
    #     return result

    def call_math_api(self, query: str):
        print("\n=================Calling math API=================")
        print(query)
        params = {"appid": '74UV94-Q95PR46UGT', "i": query, "format": "Mathematica"}
        result = self.make_request("http://api.wolframalpha.com/v2/result", params)
        if result is None:
            result = "Error: Invalid expression"
        # else:
        #     result = result.strip()
        #     # parse the result using SymPy to get it in the desired format
        #     expr = sp.S(str(result))
        #     formatted_result = sp.pretty(expr)
        #     result = formatted_result.replace("==", "=")
        return result

    def clear_toolKit(self):
        self.variables.clear()
    
#tool = ToolKit()
#print(tool.call_math_api('solve x^2 = 4'))

equation = "solve 8x+2y+3z=12, 3x+4y+5z=13, 5x+6y+7z=14"
query = urllib.parse.quote_plus(equation)
query_url = f"http://api.wolframalpha.com/v2/query?" \
            f"appid={'74UV94-Q95PR46UGT'}" \
            f"&input={query}" \
            f"&includepodid=Result" \
            f"&output=json"

r = requests.get(query_url).json()

data = r["queryresult"]["pods"][0]["subpods"][0]
plaintext = data["plaintext"]

print(plaintext)
# Result of 7 + 2x = 12 - 3x is 'x = 1'.
