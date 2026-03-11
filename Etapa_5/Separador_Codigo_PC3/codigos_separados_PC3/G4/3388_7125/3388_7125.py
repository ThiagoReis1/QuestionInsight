var1 = input("unidade de medida:")
var2 = float(input("valor:"))

if var1.upper() == "B" :
	print(round(var2/3.41214,2))
if var1.upper() == "W" :
	print(round(var2*3.41214,2))

