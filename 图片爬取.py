import os

import bs4
import requests

baseUrl = "https://imgur.com"
url = baseUrl + "/search/score?q=" + "movie"
dirName = 'image'
os.makedirs(dirName,exist_ok=True)
response_get = requests.get(url) 
response_get.raise_for_status()
soup = bs4.BeautifulSoup(response_get.text,'html.parser')
imageUrls = soup.select(".image-list-link img")
if not imageUrls:
        print("没有找到这个图片的标签")
else:
    for imageUrl in imageUrls:
        downloadUrl = imageUrl.get('src')
        print("下载图片的路径：",downloadUrl)
        # 分割字符
        split=downloadUrl.split('/')
        fileName = os.path.basename(split[len(split)-1])
        
        # 文件路径
        filePath=os.path.join(dirName,fileName)
        # 检查文件路径是否存在
        if not os.path.exists(filePath):
               imagePath = requests.get("https:"+downloadUrl)
               print("请求：",imagePath)
               imageFile = open(filePath,"wb")
               for images in imagePath.iter_content(2000):
                       # 把每次遍历的文件全部写入文件夹中
                       imageFile.write(images)
                
