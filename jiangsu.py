import requests
import re
from bs4 import BeautifulSoup

url = "http://www.jiangsu.gov.cn/col/col31255/index.html"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

latest_news = soup.find_all('a', {'title': '《江苏省农村土地经营权流转管理办法》（省政府令第180号）'})
print(latest_news)