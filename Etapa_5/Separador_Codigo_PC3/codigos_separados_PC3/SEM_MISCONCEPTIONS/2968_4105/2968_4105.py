valor=input("Pedido? (L/S): ")
x= float(input("Quantidades de (L/S): "))
y= float(input("Quantidades de Refrigerante: "))

if(valor.upper() == "L"):
	valor= x*5+y*4
print(round(valor,2))
	
