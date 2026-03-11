var1 = float(input("deposito inicial: "))
n = int(input("meses: "))


mes = 0
juros = 0.01

while mes < n:
	mes = mes + 1
	var1 = var1 + (var1 * juros)
	
	print(round(var1,2))