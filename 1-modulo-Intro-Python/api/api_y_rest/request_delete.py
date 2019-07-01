import requests

url = "https://jsonplaceholder.typicode.com/posts/20"

payload = "{\n\t\n}"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "77d22990-9bf1-41eb-a117-0ec5017ad633"
    }

response = requests.request("DELETE", url, data=payload, headers=headers)

print(response.text)