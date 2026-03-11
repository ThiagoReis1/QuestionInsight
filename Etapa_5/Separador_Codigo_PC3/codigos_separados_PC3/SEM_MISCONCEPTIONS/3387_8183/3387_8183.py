var1 = input("informe a medidade (M / K): ")
var2 = float(input("Informe o valor da medida: "))


if (var1.upper() == 'K'):
	conversao = 2.35215 * var2
	
else: 
	conversao = var2 / 2.35215
	
print(round(conversao, 2))
