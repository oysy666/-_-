import requests
url='https://my.4399.com/'
#通过第一种方式请求头中携带cookie进行构造
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    'cookie':'Hm_lvt_f1fb60d2559a83c8fa1ee6125a352bd7=1770545980; UM_distinctid=19c3cc3a1ad5b2-08266a24fd8d8-4c657b58-151800-19c3cc3a1ae1c68; _4399tongji_vid=17705460285426; _4399stats_vid=17705460290408432; Puser=19558719032; Qnick=; _gprp_c=""; index4399skintip=1; home4399=yes; Hm_lvt_334aca66d28b3b338a76075366b2b9e8=1770546247,1771905771; Hm_lpvt_334aca66d28b3b338a76075366b2b9e8=1771905771; HMACCOUNT=9BE690E20CB4A4FF; USESSIONID=1c3a1038-be0b-42f7-b018-e67a0a054003; Uauth=4399|1|2026224|www_home.|1771905788903|865218bc4c2fe6c5a2b44908c2547f23; Pauth=1237066886|3996206118|t3ce7n53361aad84eea004d4b744e87d|1771905788|10002|3a6037d10c9597f9fee425f47141e8bc|2; ck_accname=3996206118; Xauth=0f5df85ff095e03ead016c6262de09ad; ptusertype=www_home.phone_login; Sauth=1237066886%7C3996206118%7C1771905788%7C1772769791%7C2f554d197f1146903cd7%7C%7C3996206118%7C537069934dd38cf018581aed0aea550e; Pnickset=1; zone_guide_date=1771948800; zone_guide_time=1; _4399tongji_st=1771905795; Hm_lvt_e5a07b5994f78634294b9c347a5be7d2=1770546029,1771905795; Hm_lpvt_e5a07b5994f78634294b9c347a5be7d2=1771905795; Hm_lvt_5c9e5e1fa99c3821422bf61e662d4ea5=1770546029,1771905795; Hm_lpvt_5c9e5e1fa99c3821422bf61e662d4ea5=1771905795; Pmtime=24e0e156e8f23ee47165%7C1771905797; ol=1'

}
response=requests.get(url=url,headers=headers)
response.encoding='utf-8'
print(response.text)
