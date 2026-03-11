pedido = input("").upper()

if pedido =="T":
	tapioca= int(input())
	acai = int(input())
	total = tapioca*5.5 + acai*10
	
else:
	salgado = int(input())
	acai = int(input())
	total = salgado*4+acai*10
	
print(round(total,2))

	