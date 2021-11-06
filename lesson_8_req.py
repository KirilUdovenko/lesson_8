import requests

url = "http://api.formatic.com/api/1.0/"
params = {"method": "getQuote",
          "format": "json",
          "lang": "ru"}


r = requests.get(url, params=params)

print(r.status_code)

print(r.json())