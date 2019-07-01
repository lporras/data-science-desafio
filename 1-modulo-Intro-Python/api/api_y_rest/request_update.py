import requests

url = "https://jsonplaceholder.typicode.com/posts/20"

payload = "{\n\t\"title\": \"nuevo titulo\",\n\t\"body\": \"Esto es un cambio\",\n\t\"userId\": 1\n}"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "e1d01d04-f3e7-4c36-b8ac-e64f77a73300"
    }

response = requests.request("PUT", url, data=payload, headers=headers)

print(response.text)