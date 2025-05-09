# Contar vocales de una cadena

cadena = input("Ingrese una cadena: ")
vocales = "aeiou"
conteo = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for letra in cadena.lower():
    if letra in vocales:
        conteo[letra] += 1

for vocal in vocales:
    print(f"{vocal}: {conteo[vocal]}")