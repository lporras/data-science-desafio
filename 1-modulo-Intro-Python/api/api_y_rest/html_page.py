from request_func import request

data = request("https://jsonplaceholder.typicode.com/photos")[:10]

html = ""

for photo in data:
    html += "<img src=\"{}\"\>\n".format(photo["url"])

with open("output.html", "w") as f:
    f.write(html)