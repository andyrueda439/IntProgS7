#Promedio de N calificaciones

n = int(input("Ingrese la cantidad de calificaciones: "))
suma = 0

for i in range(n):
    calificacion = float(input(f"Ingrese la calificación #{i+1}: "))
    suma += calificacion

promedio = suma / n
print("El promedio es:", promedio)