numero = int(input("informe o numero"))
parte1 = numero // 1000
parte2 = numero % 1000
if ((parte1 - parte2) ** 2 == numero):
	print(numero, " atende a propriedade")
else:
	print((parte1 - parte2) ** 2)