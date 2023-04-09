import wikipediaapi

class ToolKit():
    def __init__(self):
        pass

    def call_wiki_API(self, query: str):
        wiki_wiki = wikipediaapi.Wikipedia('en')
        # search for pages related to 'python'
        search_results = wiki_wiki.search(query)

        # print the title and summary of each search result
        # for result in search_results:
        #     page = wiki_wiki.page(result)
        #     print(page.title, ":", page.summary)
        #     page = wiki_wiki.page(search)
        page = wiki_wiki.page(search_results[0])
        return page.summary

    # TODO : Complete qa API and improve math API
    def call_qa_api(self, query: str):
        # is that google api?
        pass

    def call_math_api(self, query: str):
        try:
            result = str(eval(query))
        except:
            result = "Error: Invalid expression"
        return result
    