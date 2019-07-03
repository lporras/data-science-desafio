import requests
import json
from os import environ
default_key = ""

if 'NASA_KEY' in environ.keys():
  default_key = environ['NASA_KEY']

#print("default_key: {}".format(default_key))

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000"

def request(url, api_key=default_key):
  headers = {
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "4b355524-bbf4-4532-a281-9269f6b57fe9,fcf39638-f5e6-4e65-a8f2-ea23eb9c2970",
    'Host': "api.nasa.gov",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
  }
  querystring = {
    "api_key": api_key,
    "total_photos": 5,
    "page": 1
  }
  response = requests.request("GET", url, headers=headers, params=querystring)
  return json.loads(response.text)

def build_web_page(response):
  html = "<html>\n<head>\n</head>\n<body>\n<ul>\n"
  lis = ""
  if "photos" in response:
    for photo in response["photos"]:
      lis += "<li><img src='{}'></li>\n".format(photo["img_src"])
  html += lis
  html += "</ul>\n</body>\n</html>"
  print("html: {}".format(html))
  with open("output.html", "w") as f:
    f.write(html)

def photos_count(response):
  result = {}
  if "photos" in response:
    for photo in response["photos"]:
      if photo["camera"]["name"] in result:
        result[photo["camera"]["name"]] += 1
      else:
        result[photo["camera"]["name"]]= 0
  return result

build_web_page(request(url))
print(photos_count(request(url)))