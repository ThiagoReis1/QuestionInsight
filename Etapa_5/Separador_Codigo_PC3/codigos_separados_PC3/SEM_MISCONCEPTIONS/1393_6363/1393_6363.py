grama = float(input("valor da grama: "))

if(grama<5000):
	valor = grama*0.05
	print(round(valor, 2))
else:
	valor = (grama*0.04)+60.0
	print(round(valor, 2))
	