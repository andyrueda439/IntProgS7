# Calcular la frecuencia de cada digito en un numero

numero = input("Ingrese un número entero: ")
frecuencias = [0] * 10

for digito in numero:
    if digito.isdigit():
        frecuencias[int(digito)] += 1

for i in range(10):
    print(f"Dígito {i}: {frecuencias[i]}")