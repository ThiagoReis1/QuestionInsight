a = int(input("quantas aboboras foram compradas: "))
preco1 = 3.80
preco2 = 3.45
if (a<5):
	calculo = (a * (preco1))
else:
	calculo = (a * (preco2))

print(round(calculo, 2))
