import requests
url='https://ys.endata.cn/enlib-api/api/home/getrank_mainland.do'
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
}
data={
'r': 0.15368337272489319,
'top': 50,
'type': 0
}
response=requests.get(url=url,headers=headers,data=data)
print(response.json())
