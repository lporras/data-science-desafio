import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

payload = ""
headers = {
    'cache-control': "no-cache",
    'Postman-Token': "3d304298-8c01-48d8-9a0d-5512f5a8ba9f"
    }

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)
print(response)
result = json.loads(response.text)

print(type(result))
print(result[0]["userId"])
print(result[0]["title"])

for post in result:
    print(post["title"])
# In [19]: len(result)
# Out[19]: 100

# Codigos de respuesta
# 1xx: Informacion
# 2xx: Respuesta correcta
# 3xx: Redirección
# 4xx: Error del cliente
# 5xx: Error del servidor

# 401: Se requiere autenticacion
# 200: todo bien
# 403: No tiene permisos de acceso
# 404: no encontrado