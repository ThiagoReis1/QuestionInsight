idade= int(input("idade do garoto ou garota: "))

if idade < 12:
	valor_ing = 20 + 1.25
	print(round(valor_ing, 2))
	
elif idade == 12:
	valor_ing = 20 + 2.25
	print(round(valor_ing, 2))
	
else:
	valor_ing = 20 + 3.25
	print(round(valor_ing, 2))