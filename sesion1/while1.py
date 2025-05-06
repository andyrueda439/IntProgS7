"""Leer una palabra diferente a fin y conertirla a mayuscula"""

palabra = input("Dime una palabra: ")
while palabra.lower() != "fin":
    print(f"{palabra.upper()} tiene {len(palabra)} letras")
    palabra = input("Dime una palabra: ")
else:
    print("Bye bye")