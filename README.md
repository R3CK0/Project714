To use the code you must first obtain 3 api keys which you will need to run the different parts of the code.

Serp api

Open the Google API Console or https://serpapi.com/ .
Create an account and verify you email and phone number.
Obtain your API key with other parameters.

it should look like this;

params = {
    "q": “”,
    "location": "Austin, Texas, United States",
    "hl": "en",
    "gl": "us",
    "google_domain": "google.com",
    "api_key": "your secret_api_key "
}

Open Api

Visit the OpenAI website and sign up for an account.
after signing in, on the right side, click on the Personal and navigate to view API keys
click create new secret key and a new key will be generated 
copy the key and keep it in a notepad file 


Wolfram Api

create a wolframe account https://developer.wolframalpha.com/portal/myapps/index.html
on the right side, Click on get an AppID
fill in the Application name and description of the project to get AppID
A small window with app name, APPID, and usage type will be popped up 


Once you have obtained and placed you API keys in the correct places, you must intall the requirements found in requirements.txt in the DATU_GPT folder. Once you are done configuring your environnement you may execute the main in your favorite IDE or directly in the terminal, select the model you wish to use and ask your question away.

**Note that without a paid subscription to OpenAI's API you might not be able to use the decomposition model or complex model since it may produce requests faster then you are alloted. Also the free SERPAPI account will only allow you 100 requests per month so be aware if heavily testing.
