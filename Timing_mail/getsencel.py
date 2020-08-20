import requests
from bs4 import BeautifulSoup

def getHtml(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
               (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    
    response = requests.get(url,headers = headers)
    response.encoding = "GB2312"
    htmlText = response.text
    return htmlText



def __sloveHtml(htmlText):
    soup = BeautifulSoup(htmlText,"html.parser")
    div_node = soup.find('div', class_='content')
    p_node = div_node.find_all('p')
    
    sentenceList = list()
    
    for content in p_node:
        [s.extract() for s in div_node('u')]
        text = content.get_text().split("、",1)[1]
        sentenceList.append(text)

    return sentenceList

def getSentenceList(url):
    html = getHtml(url)
    sentenceList = __sloveHtml(html)
    return sentenceList