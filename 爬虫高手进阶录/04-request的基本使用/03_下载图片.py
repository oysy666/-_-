import requests
#设置url
url='https://www.baidu.com/img/flexible/logo/pc/result@2.png'
#发起请求
response=requests.get(url=url)
#存储本地
with open('x.jpg','wb') as f :
    f.write(response.content)
