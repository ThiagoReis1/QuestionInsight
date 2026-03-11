algarismo_1 = int(input("Forneca um numero: "))

valor_1 = algarismo_1//100
valor_2 = (algarismo_1%100)//10
valor_3 = (algarismo_1%100)%10

numero_fornecido = (valor_1**3 + valor_2**3 + valor_3**3)

if(numero_fornecido==algarismo_1):
	print(algarismo_1)
	print("atende")
else:
	print(algarismo_1)
	print("nao atende")