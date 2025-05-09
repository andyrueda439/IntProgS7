#Simulacion de un cajero automatico

saldo = 100

while True:
    print(f"\nSaldo actual: ${saldo}")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        saldo += cantidad
    elif opcion == "2":
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        if cantidad <= saldo:
            saldo -= cantidad
        else:
            print("Fondos insuficientes.")
    elif opcion == "3":
        print("Gracias por usar el cajero. Saldo final:", saldo)
        break
    else:
        print("Opción inválida.")