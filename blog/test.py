import requests

headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
url="http://localhost:8000/api-token-auth/"
post_data={"username":"admin","password":"123456"}
res=requests.post(url,post_data,headers=headers)
print(res.text)
