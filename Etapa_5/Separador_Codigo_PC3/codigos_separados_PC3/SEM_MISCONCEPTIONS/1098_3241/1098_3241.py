numero = str(input())

senha1 = int(numero[0]) + int(numero[1]) + int(numero[2])
senha2 = int(numero[3]) + int(numero[4]) + int(numero[5])
calculo = (senha1 - senha2) ** 4 

if (calculo == numero):
	print(numero)
	print("atende")
else:
	print(numero)
	print("nao atende")
