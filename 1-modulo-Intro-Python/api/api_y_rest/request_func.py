import json
import requests

def request(requested_url):
    payload = ""
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "3d304298-8c01-48d8-9a0d-5512f5a8ba9f"
        }
    response = requests.request("GET", requested_url, data=payload, headers=headers)
    return json.loads(response.text)

#print(request("https://jsonplaceholder.typicode.com/posts"))
#print(request("https://jsonplaceholder.typicode.com/photos")[:10])