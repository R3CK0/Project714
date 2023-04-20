import wikipediaapi
import urllib.parse
import requests
from serpapi import GoogleSearch

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
        print("variables: ", self.variables)
        print("\n=================Calling SERP API=================")
        print(query)
        params = {
            "q": query,
            "location": "Austin, Texas, United States",
            "hl": "en",
            "gl": "us",
            "google_domain": "google.com",
            "api_key": "3df9d9a99f885a6e90092a5bddf979d38d14ac33cd4b3a33f098cd2acc373ba4"
        }

        search = GoogleSearch(params)

        results = search.get_dict()
        try:
            result = results['answer_box']['snippet_highlighted_words']
        except:
            try:
                result = results['answer_box']['snippet']
            except:
                result = "[This type of question is not supported yet]"
        res = ''.join(result)
        return res
        # return input(query + " : ")
        # return "replace this part using you best judgement"

    

    def call_math_api(self, query: str):
        print("variables: ", self.variables)
        print("\n=================Calling math API=================")
        print(query)
        params = {"appid": '74UV94-Q95PR46UGT', "i": query}
        result = self.make_request("http://api.wolframalpha.com/v2/result", params)
        if result is None:
            result = "Error: Invalid expression"
        return result


    def solve_math_api(self, query:str):

        query = urllib.parse.quote_plus(query)
        query_url = f"http://api.wolframalpha.com/v2/query?" \
                    f"appid=74UV94-Q95PR46UGT" \
                    f"&input={query}" \
                    f"&includepodid=Result" \
                    f"&output=json"

        r = requests.get(query_url).json()

        data = r["queryresult"]["pods"][0]["subpods"][0]
        results = data["plaintext"]
        variables = results.split(" and ")
        for var in variables:
            pair = var.split(" = ")
            key = pair[0]
            val = pair[1]
            self.variables[key] = val
        return results

    def clear_toolKit(self):
        self.variables.clear()


# tool = ToolKit()
# print(tool.call_math_api('d(7x)/dx'))
