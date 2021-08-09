import requests
from lxml import etree
import random
s = requests.Session()
random_num = random.random()
url = f'https://mall.jd.com/sys/vc/createVerifyCode.html?random={random_num}'
code_img_url = s.get(url)

with open('jd_code.jpg','wb') as f:
    f.write(code_img_url.content)
code = input('输入验证码：')
param = {"verifyCode":code}
start_url = 'https://mall.jd.com/showLicence-649114.html'
get_detail = s.post(url=start_url,data=param).text
print(get_detail)