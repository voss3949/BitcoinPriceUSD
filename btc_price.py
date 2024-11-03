import requests
from bs4 import BeautifulSoup

url = "https://exchange.blockchain.com/"

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'html.parser')

btc_price = soup.find('td', {'class': 'PricesTable__PriceCol-p25khh-9 foKaFp'})



