numero = float(input("string"))

n100 = numero // 100
resto = n100 % 1000
propriedade = n100 ** 2 + resto ** 2 

if (numero == propriedade):
	print(propriedade, " atende a propriedade")
else:
	print(propriedade)
