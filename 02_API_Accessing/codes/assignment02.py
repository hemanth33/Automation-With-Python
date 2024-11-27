import requests
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Access variables
api = os.getenv('api2')
zip = os.getenv('zip')

# def get_latAndLong(api, zip):
#     url = f"http://api.openweathermap.org/geo/1.0/zip?zip={zip},IN&appid={api}"
#     r = requests.get(url=url)
#     result = r.json()
#     return result["lat"], result["lon"]

url = f"http://api.openweathermap.org/data/2.5/forecast?q=Bangalore,IN&appid={api}"
r = requests.get(url=url)
result = r.json()

with open('data.txt', 'a')as file:
    for dicty in result['list']:
        file.write(f"{dicty['dt_txt']},{dicty['main']['temp']},{dicty['weather'][0]['description']}\n")
    
    file.write(f"{result['city']['name']}")

    

