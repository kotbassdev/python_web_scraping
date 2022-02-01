import requests
from bs4 import BeautifulSoup

url = "https://365liveball.com/%E0%B8%9E%E0%B8%A3%E0%B8%B5%E0%B9%80%E0%B8%A1%E0%B8%B5%E0%B8%A2%E0%B8%A3%E0%B9%8C%E0%B8%A5%E0%B8%B5%E0%B8%81/%E0%B9%80%E0%B8%AD%E0%B8%9F%E0%B8%95%E0%B8%B1%E0%B9%89%E0%B8%87%E0%B9%81%E0%B8%A5%E0%B8%A1%E0%B8%9E%E0%B8%B2%E0%B8%A3%E0%B9%8C%E0%B8%94%E0%B8%84%E0%B8%B8%E0%B8%A1%E0%B8%97%E0%B8%B1%E0%B8%9E%E0%B8%A2%E0%B8%B7%E0%B8%A1%E0%B9%80%E0%B8%94%E0%B8%AD%E0%B9%80%E0%B8%9A%E0%B9%87%E0%B8%84%E0%B8%84%E0%B8%A7%E0%B9%89%E0%B8%B2%E0%B8%AD%E0%B8%B1%E0%B8%A5%E0%B8%A5%E0%B8%B5%E0%B9%88"
web_data = requests.get(url)

soup = BeautifulSoup(web_data.text,'html.parser')
h1 = soup.find("h1")
# print('h1:' +str(h1.text))

content = soup.find("div",{"class":"content-detail-box"})
# print(content.text)


bx_detail = soup.find("div",{"class":"bx-detail"})
img = bx_detail.find("img")
img_src = img.get('src')

img_res = requests.get(img_src)
file = open("image.jpg","wb")
file.write(img_res.content)
file.close()