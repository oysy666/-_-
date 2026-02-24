import requests#导入模块
#设置目标数据包url
bd_url='https://www.baidu.com'
#发起请求 并且接受响应
response=requests.get(bd_url)
print(response)#响应对象
print(response.status_code)#状态码
print(response.text)
print(response.encoding)
#设置编码
response.encoding='utf-8'
print(response.text)
print(response.request.headers)
