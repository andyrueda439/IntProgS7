#Producto de los primeros M numeros

M = int(input("Ingrese el numero entero M: "))
contador = 0
producto = 1 
par = 2

while contador < M:
    producto *= par
    par += 2
    contador += 1

print("El producto de los primeros", M, "numeros pares es: ", producto)