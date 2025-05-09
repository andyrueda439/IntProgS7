#Suma de los primeros numeros

N = int(input("Ingrese un numero entero positivo: "))
if N > 0:
    suma = 0
    for i in range (1, N + 1):
        suma += i
    print (f"La suma de los numeros 1 a {N} es de: {suma} ")
else:
    print("Por favor, ingrese un numero positivo")