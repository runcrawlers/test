import json
from jsonpath import jsonpath
import requests
from lxml import etree
import time
start_url = 'http://ad-api.996box.com/v1/homeapi/FindGame/getTodayNewServerList'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',

}
rq_time = str(time.time()).replace('.', '')[:14]
params = {
        "size": 10,
        "page": 2,
        "rqtime": 1631867984471,
        "rqrandom": "Ouv4ULEx52",
        "sign": "14e062e88f4c61c01331d6497a61c7f5"
}

response = requests.get(url=start_url, headers=headers, params=params).json()
print(response)
print(type(response))
data = jsonpath(response, '$..game_name')
print(data)



