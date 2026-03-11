X = int(input("Escreva um numero inteiro: "))

if X % 31 == 0:
	quo = X // 31
	print(quo)
	print("sim")
else:
	rest = X % 31
	print(rest)
	print("nao")