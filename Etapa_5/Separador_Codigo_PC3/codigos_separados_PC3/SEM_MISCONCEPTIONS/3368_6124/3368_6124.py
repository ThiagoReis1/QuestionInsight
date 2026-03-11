escala = input("Escala em que a temperatura esta representada for 'C' ou 'K': ")
valor = float(input("Valor da temperatura: "))

if escala == 'C':
	K = valor + 273.15
	print(round(K, 2))
else:
	K = valor - 273.15
	print(round(K, 2))