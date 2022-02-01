import requests 
from bs4 import BeautifulSoup

url = "https://365liveball.com/%E0%B8%9E%E0%B8%A3%E0%B8%B5%E0%B9%80%E0%B8%A1%E0%B8%B5%E0%B8%A2%E0%B8%A3%E0%B9%8C%E0%B8%A5%E0%B8%B5%E0%B8%81"
web_data = requests.get(url)
# print(web_data.status_code)
# print(web_data.text)

soup = BeautifulSoup(web_data.text,'html.parser')
find_words = soup.find_all("a",{"class":"a-wrap"})

for el in find_words:
    print(el.get('href'))