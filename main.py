import requests
from bs4 import BeautifulSoup
from urllib.parse import parse_qs, urlparse
import warnings

iTaiwansPhoneNumber = "09xxxxxxxx" #必須是要有註冊過iTaiwan帳號的手機號碼
iTaiwansPassword = "xxxxxxxxxxxxx" #此手機號的iTaiwan密碼

warnings.filterwarnings("ignore")

site = "http://172.217.160.110/"   #這是測試是否要登入
authdata = {"username": iTaiwansPhoneNumber + "@itw", "password": iTaiwansPassword, "popup": "true"}
respond = requests.get(site, verify=False)
if respond.url != site:
    logurl = urlparse(respond.url).query
    logurl = parse_qs(logurl, keep_blank_values=True)
    logurl = logurl["loginurl"][0]
    print(logurl)
    ot2 = requests.post(logurl, data=authdata, verify=False)
    if ot2.status_code == 200:
        soup = BeautifulSoup(ot.text, 'html.parser')
        status = soup.find("font", {"color" : "red"}).text
        if status == "無線上網認證成功！":
            print("Auth Successful!")
        else:
            print("Auth Failed!")
else:
    print("Not Needs To Auth")
