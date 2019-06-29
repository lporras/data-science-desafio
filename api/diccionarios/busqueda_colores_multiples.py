import sys
search = sys.argv[1]

searched_hexas = sys.argv[1:]

colores = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "darkorchid": "#9932cc",
    "darkred": "#8b0000",
    "darksalmon": "#e9967a",
    "navajowhite": "#ffdead",
    "navy": "#000080",
    "orchid": "#da70d6"
}

colores_inv = {v:k for k, v in colores.items()}

for search in searched_hexas:
    if search in colores_inv:
        print(colores_inv[search])
    else:
        print("no-no")


