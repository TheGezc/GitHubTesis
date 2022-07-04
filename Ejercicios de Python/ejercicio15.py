numero1 = int(input("Proporciona el numero 1: "))
numero2 = int(input("Proporciona el numero 2: "))

while True:
    if numero1>numero2:
        print("El numero mayor es: ", numero1)
    elif numero2>numero1:
        print("El numero mayor es: ", numero2)
    elif numero1==numero2:
        print("Los numeros son iguales")
    break
