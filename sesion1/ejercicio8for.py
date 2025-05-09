#Mayor y menor de n numeros

n = int(input("Ingrese la cantidad de números: "))
mayor = float('-inf')
menor = float('inf')

for i in range(n):
    numero = float(input(f"Ingrese el número #{i+1}: "))
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero

print("Mayor:", mayor)
print("Menor:", menor)