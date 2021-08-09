import requests
from concurrent.futures import ThreadPoolExecutor

def get(url):
    res = requests.get(url)
    return res

if __name__ == '__main__':
    url = 'http://172.16.61.147:5000/api/index'
    # get(url)
    pool = ThreadPoolExecutor(100)
    for i in range(10000000000000000000000000000000000000):
        pool.submit(get,url)
