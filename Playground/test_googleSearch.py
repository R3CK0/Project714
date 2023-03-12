import requests, lxml
from bs4 import BeautifulSoup

# http://httpbin.org/headers
headers = {
  'User-agent':
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

params = {
    'q': 'what is the capital of France?',
    'gl': 'ca'
}

def get_organic_result_answerbox():
  html = requests.get('https://www.google.com/search', headers=headers, params=params)
  soup = BeautifulSoup(html.text, 'lxml')

  answer = 0#soup.select_one('.IZ6rdc').text
  title = 0#soup.select_one('.DKV0Md').text
  link = soup.select_one('.yuRUbf a')['href']
  snippet = soup.select_one('.hgKElc').text
  print(f"{answer}\n{title}\n{link}\n{snippet}")

get_organic_result_answerbox()

response = requests.get('http://httpbin.org/headers', headers=headers)
print(response.json()['headers']['User-Agent'])