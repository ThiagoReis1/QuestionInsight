val_compra = float(input("digite o valor da compra: "))
cod = input("digite 'D' 'P' 'C1' 'C2': ")
if (cod == 'D'):
	y = val_compra - (val_compra * 17/100)
	print(round(y, 2))
elif (cod == 'P'):
	y = val_compra - (val_compra * 17/100)
	print(round(y, 2))
elif (cod == 'C1'):
	print(round(val_compra))
else:
	y = (val_compra * 8/100) + val_compra
	print(round(y, 2))