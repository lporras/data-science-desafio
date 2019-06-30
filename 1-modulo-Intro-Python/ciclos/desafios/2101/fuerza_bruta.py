import string
password = input("Ingresa contraseña\n")
tries = 0

for letter in password:
    for i in string.ascii_lowercase:
        tries += 1
        if i == letter.lower():
            break
print(f"{tries} intentos")