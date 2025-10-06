Precio = float(input("ingrese el precio del producto:\n"))
Cantidad = int(input("ingrese la cantidad que desea comprar:\n"))
total = Precio * Cantidad 

print(f"\n---TOTAL DE LA COMPRA---")
print(f"Compraste {Cantidad} unidades a ${Precio:,.2f} cada una")
print(f"El total a pagar es ${total:,.2f}")
