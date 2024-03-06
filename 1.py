import datetime
import os
import requests

url = 'https://d.faithxy.com/motion/api/motion/Xiaomi'
users = eval(os.environ['USERS'])

headers = {
    'Cookie': '__51vcke__Jhgumxrm39to0PvP=86a0ff22-b0ab-57c5-875a-6cc9b40179ec; __51vuft__Jhgumxrm39to0PvP=1709627962784; __51uvsct__Jhgumxrm39to0PvP=3; __vtins__Jhgumxrm39to0PvP=%7B%22sid%22%3A%20%2213dc25a0-0d48-5154-aa97-abac9f68fb3c%22%2C%20%22vd%22%3A%202%2C%20%22stt%22%3A%20774324%2C%20%22dr%22%3A%20774324%2C%20%22expires%22%3A%201709693607684%2C%20%22ct%22%3A%201709691807684%7D',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://d.faithxy.com',
    'Referer': 'https://d.faithxy.com/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh-HK;q=0.9,zh;q=0.8,en;q=0.7'
}

data={
    'phone': '547572207@qq.com',
    'pwd': 'fzx2002112588',
    'num': '15000'
}

proxies = {
    # 如果不需要代理，请将这里设置为 None
    'http': None,
    'https': None,
}

response = requests.post(url, headers=headers, data=data,proxies=proxies)

