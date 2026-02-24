import requests
#实例化一个session对象
session=requests.session()
#登录请求url
url='https://u.4399.com/login.html?refer=https%3A%2F%2Fu.4399.com%2Fprofile%2Favatar.html'
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    'cookie':'Hm_lvt_f1fb60d2559a83c8fa1ee6125a352bd7=1770545980; UM_distinctid=19c3cc3a1ad5b2-08266a24fd8d8-4c657b58-151800-19c3cc3a1ae1c68; _4399tongji_vid=17705460285426; _4399stats_vid=17705460290408432; Puser=19558719032; Qnick=; _gprp_c=""; index4399skintip=1; home4399=yes; Hm_lvt_334aca66d28b3b338a76075366b2b9e8=1770546247,1771905771; Hm_lpvt_334aca66d28b3b338a76075366b2b9e8=1771905771; HMACCOUNT=9BE690E20CB4A4FF; USESSIONID=1c3a1038-be0b-42f7-b018-e67a0a054003; Xauth=0f5df85ff095e03ead016c6262de09ad; ptusertype=www_home.phone_login; Pnickset=1; _4399tongji_st=1771905795; phlogact=l115598p15616'
}
#进行登录
session.post(url=url,headers=headers)
#登录成功后就会记录身份信息状态
print(session)