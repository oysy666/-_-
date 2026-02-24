import requests
#设置url
url='https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1771864494873&countryId=&cityId=&bgIds=&productId=&categoryId=40001001,40001002,40001005,40001006,40003001,40003003&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area='

headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
}
#发起请求
response=requests.get(url=url,headers=headers)
print(response.text)
print((type(response.text)))#<class 'str>
#确保数据是jason格式的。才能使用.json()
print(response.json())
print((type(response.json())))

#第二种,参数构造成参数字典 在请求时带上参数字典进行请求    较为麻烦，使用传参方式
# url='https://careers.tencent.com/tencentcareer/api/post/Query'


