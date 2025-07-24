#Web Scraper for News Headlines code
import requests 
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
headlines = soup.find_all("h2")

with open("headlines.txt","w", encoding = 'utf-8') as f:
     for headline in headlines:
         text = headline.get_text().strip()
         if text:
            f.write(text + "\n")

print("Headlines are successfully saved")
