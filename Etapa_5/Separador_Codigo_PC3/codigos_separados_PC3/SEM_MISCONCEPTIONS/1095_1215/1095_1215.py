numeros = int(input("X igual a:"))
n1000 = numeros // 10000
resto = numeros % 10000
propriedade = (n1000 + resto) ** 2
if(propriedade == numeros):
	print(propriedade, "X atende a propriedade")
else:
	print(propriedade)