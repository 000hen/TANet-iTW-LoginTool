import requests
from bs4 import BeautifulSoup
from urllib.parse import parse_qs, urlparse
import warnings

iTaiwansPhoneNumber = "09xxxxxxxx" #必須是要有註冊過iTaiwan帳號的手機號碼
iTaiwansPassword = "xxxxxxxxxxxxx" #此手機號的iTaiwan密碼

warnings.filterwarnings("ignore")

site = "http://clients1.google.com/generate_204"   #這是測試是否要登入
authdata = {"username": iTaiwansPhoneNumber + "@itw", "password": iTaiwansPassword, "popup": "true", "session": ""}


def logPst(logurl = "", itwlog=False):
    if (itwlog == True) & (logurl == ""):
        logurl = "https://wlanac.hinet.net/loginpages/userlogin.shtml"

    ot2 = requests.post(logurl, data=authdata, verify=False)
    if (ot2.status_code == 200) & (itwlog != True):
        soup = BeautifulSoup(ot2.text, 'html.parser')
        status = soup.find("font", {"color" : "red"}).text
        if status == "無線上網認證成功！":
            print("Auth Successful!")
            return False
        else:
            print("Auth Failed! Trying To Login...")
            return True
        
    elif (ot2.status_code == 200) & (itwlog == True):
        if (urlparse(ot2.url).path == "/auth_fail.php"):
            print("Auth Failed! Trying To Login...")
            return True
        else:
            print("Auth Successful!")
            return False


respond = requests.get(site, verify=False)
returnurl = urlparse(respond.url)
returnurl = returnurl.netloc

if respond.url != site:
    print("Needs To Login")
    logurl = urlparse(respond.url).query
    logurl = parse_qs(logurl, keep_blank_values=True)
    logurl = logurl["loginurl"][0]
    print("Found Login URL: {}, Trying To Login...".format(logurl))
    
    if (returnurl == "auth.itaiwan.gov.tw"):
        itw = True
    else:
        itw = False

    h = True
    while h:
        h = logPst(logurl, itw)

else:
    print("Not Needs To Auth")
