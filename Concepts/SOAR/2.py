import requests
import pandas as pd
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
quotes=[]
author=[]
url = "https://quotes.toscrape.com/"
response = requests.get(url,headers=headers ).text
webpage=BeautifulSoup(response, 'lxml')
for i in webpage.find_all("div", class_="quote"):
  quotes.append(i.find('span', class_='text').text)
  author.append(i.find('small', class_='author').text)

print(pd.DataFrame({'quotes':quotes,'author':author}))