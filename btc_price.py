import requests
import pandas as pd

# Step 1: Fetch JSON data from the webpage
url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
response = requests.get(url)
data = response.json()

USD_price = data['bpi']['USD']['rate']
USD_price
