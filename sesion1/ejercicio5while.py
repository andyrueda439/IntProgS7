#Factorial de un numero

n = int(input("Ingrese un número entero positivo: "))
factorial = 1
contador = 1

while contador <= n:
    factorial *= contador
    contador += 1

print(f"El factorial de {n} es: {factorial}")