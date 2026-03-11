ataque = (input("Digite tipo do ataque: "))
d1 = int(input("valor1: "))
d2 = int(input("valor2:"))
d3 = int(input("Valor3: "))
d4 = int(input("valor4: "))

if(ataque == "espada"):
	pf = (d1 + 6) + (d2+6)+ (d3 + 6)+ (d4 + 6)
	print(pf)
else:
	pf = (d1 + d2 + d3) * d4
	print(pf)