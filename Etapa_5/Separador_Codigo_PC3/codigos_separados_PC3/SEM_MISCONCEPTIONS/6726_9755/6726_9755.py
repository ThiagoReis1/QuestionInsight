X = int(input("digite seu numero: "))

b = 29

if X%b == 0:
	conta = X//29
	print(conta)
	print("sim")
else:
	conta2 = X%29
	print(conta2)
	print("nao")