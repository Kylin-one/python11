import json
import time

import requests
from lxml import etree
# 模拟浏览器
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36'}

def getOnePage(url):

    html = requests.get(url,headers = header) # 反爬虫
    
    return html.text

def parseOnePage(text):

    html = etree.HTML(text)
    # 取出电影名
    name = html.xpath('//p[@class="name"]//text()')
    # 取出主演
    star = html.xpath('//p[@class="star"]//text()')
    #取出上映时间
    releasetime = html.xpath('//p[@class="releasetime"]//text()') 

    print(releasetime)
    for item in range(len(name)):
        yield {
            'index': item,
            'name': name[item],
            'star': star[item].strip(),
            'releasetime': releasetime[item]
            }

def writeFile(content):
    with open(r'G:\python\猫眼.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii= False) + '\n')
def main():

    for offset in range(10):
        time.sleep(1)
       
        url = 'http://maoyan.com/board/4?offset={}'.format(offset*10)
        
        text = getOnePage(url)

        for item in parseOnePage(text):
            writeFile(item)
            print(item)

if __name__ == '__main__':

    main()
