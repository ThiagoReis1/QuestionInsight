var = input("digite: ")
var1= float(input("digite o valor: "))
kg = var1 * 2.20462
total = var1 / 2.20462

if var.upper() == "L":
	print(round(total, 2))
else:
	print(round(kg, 2))