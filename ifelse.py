numero1 = int(input("Digite el Primer Numero: "))
numero2 = int(input("Digite el Segundo Numero: "))

if numero2 == 0:
    print("Error: No se puede dividir por cero.")

else:
    total = numero1 / numero2
    print(f"El total es: {total}")