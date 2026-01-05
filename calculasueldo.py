Salario_mensual = int (input ("¿Cual es tu salario mensual?: "))
Costo_imagen = int (input ("¿Cual es tu presupuesto de imagen?: "))
Costo_viaje = int (input ("¿Cual es tu presupuesto de viaje: "))

#Logica de negocio
ahorro_imagen = Salario_mensual * 0.30
ahorro_viaje = Salario_mensual * 0.20

#Calculo de tiempo
tiempo_imagen = Costo_imagen / ahorro_imagen
tiempo_viaje = Costo_viaje / ahorro_viaje

print("Para renovar tu imagen necesitas",round(tiempo_imagen, 1),"meses")
print("Para tu viaje necesitas", round(tiempo_viaje, 1),"meses")