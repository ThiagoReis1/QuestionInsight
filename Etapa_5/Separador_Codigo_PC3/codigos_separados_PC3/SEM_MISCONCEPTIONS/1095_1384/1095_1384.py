numero = int(input(" Qual  o valor do numero: "))
formula = (numero // 2550 + 2500 % numero) **2

if (numero == formula):
	print("X atende a propriedade")
else:
	print("formula")