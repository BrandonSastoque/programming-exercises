precio = float(input("Digite el precio del articulo:"))
edad = int(input("Digite su edad: "))
descuento = precio * 0.90

if edad <= 18:
    print ("La venta esta prohibida para este usuario")
    
elif edad >= 60:
    print (f"Para este usuario el producto le cuesta ${descuento:,.2f}")
    
else:
    print ("El usuario puede comprar el producto pero no aplican descuentos")