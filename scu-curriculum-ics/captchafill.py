# coding:utf-8


"""
this is the module to
Identificate verification code using the api of "http://www.damagou.top/"
"""

import base64
import requests
from PIL import Image
from io import BytesIO
from random import choice


def get_english_captcha(captcha,userkey):
    base64_data = captcha
    postUrl = 'http://www.damagou.top/apiv1/recognize.html'
    postData = {
        "image": base64_data,
        "userkey": userkey,
        "type": "1001",
    }
    try:
        r = requests.post(postUrl, data=postData)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
        
    except:
        print("Captcha Module Failed")
        
        
def get_usekey_damagou():
    get_url = "http://www.damagou.top/apiv1/login.html?username=futai2&password=123456"
    try:
        r = requests.get(get_url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("Invalid Userkey")

def get_captcha():
    with open("./captcha.jpg", "rb") as f:
        # b64encode是编码，b64decode是解码
        base64_data = base64.b64encode(f.read())
        # base64.b64decode(base64data)
    userkey = get_usekey_damagou()
    return get_english_captcha(base64_data,userkey)
