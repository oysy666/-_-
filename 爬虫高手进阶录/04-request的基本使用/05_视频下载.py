import requests
#设置url
url='https://kvideo01.youju.sohu.com/b97d3490-f04c-4857-9ede-aa42718fcc812_0_0.mp4?sign=d68c4ed8220cbf4fc6941e015e085317&t=1771883892'
#发起请求
response=requests.get(url=url)
#存储本地
with open('视频.mp3','wb') as f :
    f.write(response.content)
