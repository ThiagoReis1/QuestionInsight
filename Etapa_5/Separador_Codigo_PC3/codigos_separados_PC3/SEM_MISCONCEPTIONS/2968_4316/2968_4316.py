var1 = input("L/S: ")
var2 = float(input("quantidade de lanches ou salgados:"))
var3 = float(input("a quantidade de refrigerantes: "))

total1 = var2 * 5.00 + var3 * 4.00
total2 = var2 * 3.50 + var3 * 4.00

if (var1.upper() == "L"):
	print(total1)
else:
	print(total2)
	 

