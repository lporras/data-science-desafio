import sys

search = sys.argv[1]

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

found = False

for name, hexa in colores.items():
    if hexa == search:
        found = True
        print(name)

if not found:
    print("no-no")

#(base) ➜  data-science-desafio git:(master) ✗ python api/diccionarios/busqueda_colores.py "#000080"
#navy