numero = str(input())

senha1 = float(numero[0]) + float(numero[1]) + float(numero[2])
senha2 = float(numero[0]) + float(numero[1]) + float(numero[2])
calculo = (senha1 - senha2) ** 2

if (numero == calculo):
	print("atende")
	print(numero)
else:
	print("nao atende")
	print(numero)