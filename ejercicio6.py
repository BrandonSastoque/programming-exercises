meta = float(input("¿Cual es tu meta de ahorro?: "))
total_ahorrado = 0

while total_ahorrado < meta:
    deposito = float(input("¿Cuanto depositas hoy?: "))
    total_ahorrado += deposito
    print(f"Llevas ahorrado: ${total_ahorrado}")

print("¡Felicidades! Alcanzaste tu meta")
