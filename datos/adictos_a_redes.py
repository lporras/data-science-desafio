def adictos_a_redes(lista):
    results = []
    for i in lista:
        if i > 90:
            results.append("mal")
        else:
            results.append("bien")
    return results

lista_adictos = [120, 50, 600, 30, 90, 10, 200, 0, 500]

print(adictos_a_redes(lista_adictos))

#---------------------------------------

def scan_addicts2(lista):
    results = []
    for i in lista:
        if i >= 180:
            results.append("Mal")
        elif i >= 90:
            results.append("Mejorable")
        else:
            results.append("Bien")
    return results

lista_adictos = [120, 90, 600, 30, 90, 10, 200, 180, 500]

print(scan_addicts2(lista_adictos))

#--------------------------------------

def to_minutes(lista):
    results = []
    for i in lista:
        results.append(i // 60)
    return results

seconds = [100, 50, 1000, 5000, 1000, 500]

print(to_minutes(seconds))