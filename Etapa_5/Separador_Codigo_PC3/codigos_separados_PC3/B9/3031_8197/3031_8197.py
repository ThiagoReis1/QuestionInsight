valor_x = float(input("Digite um numero com duas casas decimais: "))

if (valor_x <= 1):
	print("1")
elif (valor_x > 1 and valor_x <= 2):
	print("2")
elif (valor_x > 2 and valor_x <= 3):
	print(round(valor_x * valor_x, 2))
else:
	print(round(valor_x * valor_x * valor_x, 2))