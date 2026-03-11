x = float(input("Digite o numero: "))		 		 

if (x >= -4) and (x < 0):
	valor = (abs(x) ** (0.5))
	print(round(valor, 4))
elif (x >= 0) and (x <= 4):
	valor = x ** 0.5
	print(round(valor, 4))
else:
	print("entrada invalida")