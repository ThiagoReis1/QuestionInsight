ent = input("a,b,c,d,e: ")
quant = float(input("quantas: "))

valor = 25.9

if ent.upper() == "B" :
	preco = valor * quant - 0.10 * valor * quant
	print(round(preco,2))

else : 
	total = valor * quant
	print(round(total,2))