numeros = int(input("Digite 3 algarismos: "))
n100 = numeros // 100
rn100 = numeros % 100
n10 = rn100 // 10
rn10 = rn100 % 10
n1 = rn10 // 1
propriedade = n100 ** 3 + n10 ** 3 + n1 ** 3
if(propriedade == numeros):
	print(propriedade, "atende a propriedade")
else:
	print(propriedade)
