valor1 = float(input("primeiro valor"))
valor2 = float(input("o segundo valor"))
valor3 = float(input("o terceiro valor"))
valor_total = float(input("o valor total"))
total_compra = valor1 + valor2 + valor3
if (total_compra > valor_total):
	print(round(valor_total , 2))
	print("Sim")
else:
	print(round(valor_total , 2))
	print("Nao")