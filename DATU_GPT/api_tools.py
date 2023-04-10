import wikipediaapi
import urllib.parse
import requests

class ToolKit():
    def __init__(self):
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
        print("QA API not implemented yet")
        return input(query + " : ")
        # return "replace this part using you best judgement"

    

    def call_math_api(self, query: str):
        params = {"appid": '74UV94-Q95PR46UGT', "i": query}
        result = self.make_request("http://api.wolframalpha.com/v2/result", params)
        if result is None:
            result = "Error: Invalid expression"
        #result = str(eval(query))
        return result
    

    