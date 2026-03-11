numero = int(input("Digite o numero desejado"))
n = numero // 10000
resto = numero % 100
resto1 =  resto // 10
propriedade = ((n)**3) + ((resto)**3) + ((resto1)**3)
if(propriedade == numero):
	print(numero, "atende a propriedade")
else:
	print(propriedade)
