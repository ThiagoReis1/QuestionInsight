numeros = float(input("string"))
n1000 = numeros // 1000
resto = numeros % 1000
propriedade = (n1000 - resto) ** 2
if(propriedade == numeros):
   print(numero, "X atende a propriedade")
else:
	print(propriedade)