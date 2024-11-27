import requests
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Access variables
api = os.getenv('api1')

r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={api}")

content = r.json()

print(content['articles'])