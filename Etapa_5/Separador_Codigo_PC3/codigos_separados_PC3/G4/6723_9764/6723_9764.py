#Entrada
X = int(input("digite um numero: "))

if X%19 == 0:
	soma = X//19
	print(soma)
	print("sim")
else:
	soma = X%19
	print(soma)
	print("nao")