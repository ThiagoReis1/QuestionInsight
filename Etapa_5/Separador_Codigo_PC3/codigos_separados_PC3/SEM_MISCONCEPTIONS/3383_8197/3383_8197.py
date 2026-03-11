medida = input("Qual medida voce usara: L ou K? ")
valor_medida = float(input("Qual o valor da medida? "))

if (medida.upper () == "K"):
	print(round(2.20462 * valor_medida, 2))
else:
	print(round(valor_medida / 2.20462, 2))
