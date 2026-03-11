p= float(input("preco do produto: "))
codi= int(input("codigo meu nobre: "))

if p > 0:
	if codi == 1:
		frete= 10/100
		valor= (p - (p* 40/100) + (p * frete))
		print(round(valor, 2))
	elif codi == 2:
		frete= 8/100
		valor= (p - (p* 40/100)+ (p * frete))
		print(round(valor, 2))
	elif codi == 3:
		frete = 0
		valor= (p - (p * 40/100)+ (p * frete))
		print(round(valor, 2))
	elif codi == 4:
		frete = 2/100
		valor= (p-(p * 40/100) + (p * frete))
		print(round(valor ,2))
	else: 
		print("Entradas invalidas")
else:
	print("Entradas invalidas")