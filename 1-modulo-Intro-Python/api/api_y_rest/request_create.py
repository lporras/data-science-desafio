import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = "{\n\t\"title\": \"Post 101\",\n\t\"body\": \"Este es nuestro primer post\",\n\t\"userId\": 1\n}"
headers = {
    'Conten': "application/json",
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "21e46d15-2594-4114-9aa1-601feca7b364"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)