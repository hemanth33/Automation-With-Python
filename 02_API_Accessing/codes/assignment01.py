import requests
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Access variables
api = os.getenv('api1')

# r = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={api})

# content = r.json()

# print(content['articles'])

def get_news(
    topic, 
    from_date, 
    to_date, 
    language='en', api=api
    ):
    url = f"https://newsapi.org/v2/everything?q={topic}&from={from_date}&to={to_date}&pageSize=5&page=1&sortBy=popularity&apiKey={api}"
    
    r = requests.get(url=url)
    content = r.json()
    articles = content['articles']
    results = []
    
    for article in articles:
        results.append(f" 'Author: {article['author']}','Source:  {article['source']['name']}'")
    return results

result = get_news(topic='space', from_date='2024-11-01', to_date='2023-11-25')

for r in result:
    print(r)
    
    
    