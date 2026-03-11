uni = input("unidade B ou W")
valor = float(input("valor "))
if(uni == "B"):
	x = valor/3.41214
	print(round(x, 2))
else:
	y= 3.41214*valor
	print(round(y, 2))