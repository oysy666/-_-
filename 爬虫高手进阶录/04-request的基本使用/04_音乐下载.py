import requests
#设置url
url='https://m10.music.126.net/20260224001838/bfe9380dd8d9372686e39d7d7b03913a/yyaac/obj/wonDkMOGw6XDiTHCmMOi/3058423385/eee5/51a0/ca78/be3c5c5d9474d405d48320d586977b10.m4a?vuutv=edipeag29zdBqg1u3GSb6eSVI9Z0CTaFaVFJX/tpjsM5mfUqpgslBw574h7dF4aCM8GfavTdlMCn6yvuGW5zeAHHM6nBMfGWPBHjjlQMcoo=&cdntag=bWFyaz1vc193ZWIscXVhbGl0eV9leGhpZ2g'
#发起请求
response=requests.get(url=url)
#存储本地
with open('给我一个理由你忘记.mp3','wb') as f :
    f.write(response.content)
