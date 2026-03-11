tipo= (input("L para lanche e P para prato execultivo: ")).upper()
qnt= float(input("quantidade: "))
rf= float(input("quantidade de refrigerante: "))

if tipo=="L":
	x= (qnt*6)+(rf*3)
	print(round(x,2))
	
else: 
	x= qnt*13.5+rf*3
	print(round(x,2))