import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote

url = "https://365liveball.com/%E0%B8%9E%E0%B8%A3%E0%B8%B5%E0%B9%80%E0%B8%A1%E0%B8%B5%E0%B8%A2%E0%B8%A3%E0%B9%8C%E0%B8%A5%E0%B8%B5%E0%B8%81"

web_data = requests.get(url)

soup = BeautifulSoup(web_data.text,"html.parser")

links = soup.find_all('a',{"class":"a-wrap bx-row form-group"})

file = open("link_lists.txt","r",encoding="utf8")
filesread = file.readlines()
file.close()

link_last = filesread[len(filesread)-1]

def writeFileContent(_index,_link,_h1,_content):
    _file = open("content-"+str(_index+1)+".txt","w",encoding="utf8")
    _file.write("*****H1*****\n")
    _file.write(str(_h1))
    _file.write("\n\n\n")
    _file.write("*****Content*****\n")
    _file.write(str(_content))
    _file.close()

    _fileLinklist = open("link_lists.txt","a",encoding="utf8")
    _fileLinklist.write("\n")
    _fileLinklist.write(_link)
    _fileLinklist.close()


def getContent(_index,_link):
    _web_data = requests.get(_link)
    _soup = BeautifulSoup(_web_data.text,'html.parser')

    _h1 = _soup.find('h1')
    _content = _soup.find('div',{"class":"content-detail-box"})

    writeFileContent(_index,_link,_h1.text.strip(),_content.text.strip())

lists_data = []
for i,link in enumerate(links):
    if link.get('href') == link_last:
        break
    else:
        lists_data.append(link.get('href'))
        
for i,link in enumerate(lists_data[::-1]):
    print(link)
    getContent(i,link)
        


