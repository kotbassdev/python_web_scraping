import requests
from bs4 import BeautifulSoup

url = "https://365liveball.com/%E0%B8%9E%E0%B8%A3%E0%B8%B5%E0%B9%80%E0%B8%A1%E0%B8%B5%E0%B8%A2%E0%B8%A3%E0%B9%8C%E0%B8%A5%E0%B8%B5%E0%B8%81/%E0%B9%80%E0%B8%AD%E0%B8%9F%E0%B8%95%E0%B8%B1%E0%B9%89%E0%B8%87%E0%B9%81%E0%B8%A5%E0%B8%A1%E0%B8%9E%E0%B8%B2%E0%B8%A3%E0%B9%8C%E0%B8%94%E0%B8%84%E0%B8%B8%E0%B8%A1%E0%B8%97%E0%B8%B1%E0%B8%9E%E0%B8%A2%E0%B8%B7%E0%B8%A1%E0%B9%80%E0%B8%94%E0%B8%AD%E0%B9%80%E0%B8%9A%E0%B9%87%E0%B8%84%E0%B8%84%E0%B8%A7%E0%B9%89%E0%B8%B2%E0%B8%AD%E0%B8%B1%E0%B8%A5%E0%B8%A5%E0%B8%B5%E0%B9%88"
web_data = requests.get(url)

soup = BeautifulSoup(web_data.text,'html.parser')


#Read H1
h1 = soup.find("h1")
h1_text = h1.text
print('H1: '+str(h1_text))

# Write H1
file = open("data.txt","w",encoding='utf-8')
file.write("------H1-----\n")
file = open("data.txt","a",encoding='utf-8')
file.write(str(h1.text))
file.write("\n\n")

#Read Content
content = soup.find("div",{"class":"content-detail-box"})
print(content.text)

# Write Content
file.write("------Content-----\n")
file.write(content.text)
file.close()

# Read Image
bx_detail = soup.find("div",{"class":"bx-detail"})
img = bx_detail.find("img")
img_src = img.get('src')

# Download Image
img_res = requests.get(img_src)
file = open("image.jpg","wb")
file.write(img_res.content)
file.close()