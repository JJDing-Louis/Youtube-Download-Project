import urllib.request as req
import bs4

url='https://www.youtube.com/playlist?list=PL-g0fdC5RMbrYH6ie-_KvV-QCIfQ_8BLW'
request = req.Request(url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")
#print(root)
item = root.select('title')[1].text
print(item)
print(type(item))