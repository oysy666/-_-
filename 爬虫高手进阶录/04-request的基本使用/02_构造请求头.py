import requests#导入模块
#设置目标数据包url
bd_url='https://www.baidu.com'
#发起请求 并且接受响应
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'

}
response=requests.get(url=bd_url,headers=headers)
response.encoding='utf-8'#设置编码
print(response.text)