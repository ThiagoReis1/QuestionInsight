var1 = input("Unidade de medida :")
var2 = float(input("Valor da medida"))

if var1.upper() == "K" :
	x = var2 * 35.274
	print(round(x,2))

if var1.upper() == "O" :
	x = var2 / 35.274
	print(round(x,2))
