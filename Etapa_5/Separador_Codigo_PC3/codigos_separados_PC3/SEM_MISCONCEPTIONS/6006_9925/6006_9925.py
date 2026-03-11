qtde = int(input("insira o numero de batatas compradas:"))
if qtde <10:
   total = qtde * 0,90
	print( round(total, 2))
else:
	total = qtde * 0,75
	print (round(total, 2))