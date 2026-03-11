entrada = int(input())

a = entrada // 1000
b = entrada % 1000

calculo = (a + b) ** 2

if (calculo == entrada):
	print("atende")
	print(entrada)
else:
	print("nao atende")
	print(entrada)