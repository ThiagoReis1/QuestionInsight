m = input("mulher? (S/N)")
preco = float(input("valor: "))
num = int(input("n: "))
quant = preco*num 
des = (20/100)*quant

if (m == "S"):
	print(round(quant-des, 2))
else:
	print(round(quant, 2))