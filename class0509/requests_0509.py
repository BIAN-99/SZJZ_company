# -- coding: utf-8 --**
import json

import requests
from bs4 import BeautifulSoup

# 访问掘金 查看城市代码
response = requests.get('https://juejin.cn/post/7081799401546448926')
# 设置编码方式
response.encoding = 'utf-8'

bs = BeautifulSoup(response.text, 'html.parser')
city_info = bs.find(
    name='code',
    attrs={"class": "hljs language-json copyable"},
)
city_str = ''
# 遍历网页爬取的数据,通过stripped_strings获取其中文本内容,类型为字符串
for x in city_info:
    # stripped_strings一下子能取出对应目录下的所有文本，并且自动把空白去掉
    for c in x.stripped_strings:
        city_str += str(c)
# 将爬取的字符串类型的内容转化成json类型,并将多余的"\"去掉
city_json = json.dumps(city_str, indent=4, ensure_ascii=False).replace("\\", "")
# 对转化为json的内容进行切片处理
city_json = city_json[1:(len(city_json) - 5)]
# 再将json数据转换为字典类型
city_dict = json.loads(city_json)
AREAID = city_dict["山东"]["济南"]["AREAID"]
url = f'http://t.weather.sojson.com/api/weather/city/{AREAID}'
resp = requests.get(url).text
with open("weatherforcast.txt", 'w') as f:
    for x in resp:
        f.write(x)
