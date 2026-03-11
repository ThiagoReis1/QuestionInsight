x = float(input("Qual o valor das vendas: "))

if (x <= 1000):
	var1 = x * 0.05

else:
	var1 = (1000 * 0.05) + (x - 1000) * 0.1

print(round(var1, 2))