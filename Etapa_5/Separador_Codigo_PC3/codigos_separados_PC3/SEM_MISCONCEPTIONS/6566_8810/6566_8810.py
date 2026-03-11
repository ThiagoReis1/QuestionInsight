# faça seu código aqui!
p = int(input("Digite a quantidade de pecas:"))

if((p < 10)):
	valor = 30 + 3.25
	total = round(valor,2)
	print("total=", total)
elif((p == 10)):
	valor = 30 + 4.50
	total = round(valor,2)
	print("total=", total)
elif((p > 10)):
	valor = 30 + 6.00
	total = round(valor,2)
	print("total=", total)
else:
	print("Entrada invalida")