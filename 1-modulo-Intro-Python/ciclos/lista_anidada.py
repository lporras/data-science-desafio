import sys

items = int(sys.argv[1])

print("<ul>\n")

for i in range(items):
    print("\t<li>\n")
    print("\t\t<ul>\n")

    for j in range(items):
        print("\t\t\t<li> {}.{} </li>".format(i, j))

    print("\t\t</ul>\n")
    print("\t</li>\n")

print("</ul>\n")