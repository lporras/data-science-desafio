import requests
import json

url = "https://reqres.in/api/users/"

def request(method, url, payload=""):
    headers = {
        'User-Agent': "PostmanRuntime/7.15.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "5761dac7-0ece-4a15-aac5-9f1a7ba920cc,9840a5ef-d9ae-42c4-8094-5efcb066fafa",
        'Host': "reqres.in",
        'accept-encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    response = requests.request(method, url, headers=headers, data=payload)
    if  response.status_code in [200, 201] and method in ["GET", "POST", "PUT"]:
        return json.loads(response.text)
    elif response.status_code in [200, 204] and method == "DELETE":
        return response.status_code
    else:
        return response.status_code

payload = "{\"name\": \"Luis Porras\", \"job\": \"Senior Developer\"}"
print(request("GET", url)["data"])
print(request("POST", url, payload))
print(request("PUT", "{}/1".format(url), payload))
print(request("DELETE", "{}/1".format(url)))