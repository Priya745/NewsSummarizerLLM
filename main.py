from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
import requests
from send_email import send_email


load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
NEWS_API_KEY= os.getenv("NEWS_API_KEY")

url = (
    "https://newsapi.org/v2/top-headlines?"
    "category=business&"
    "language=en&"
    "pageSize=8&"
    "apiKey=" + NEWS_API_KEY
)
# Make request
r = requests.get(url)

# Get a dictionary with data
content = r.json()
articles = content["articles"]
print(articles)


#ai summarizing the news
model = init_chat_model(
    model="gemini-2.5-flash",
    model_provider="google-genai",
    api_key = GOOGLE_API_KEY
)
prompt = f"""
You're a news summarizer.
Write a short paragraph analyzing those news. Add another second paragraph to tell me how they affect the stock market.
Here are the news article:
{articles}
"""
response = model.invoke(prompt)
response_str = response.content
print(response_str)
body = ("Subject: News Summary\n\n" + response_str + "\n\n")
# print(body)

body = body.encode("utf-8")
send_email(message=body)