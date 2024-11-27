import requests

r = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=27990880a46a4e0998b2cd7d7f551fe3')

content = r.json()

print(content['articles'])