import requests

from operator import itemgetter

url = "https://hacker-news.firebaseio.com/v0/item/9884165.json"

r = requests.get(url)
print("status code: " + r.status_code)