x = int(input("digite o numero:"))
soma = x % 31
if soma == 0:
	print(x // 31 )
	print("sim")
else:
	print(x % 31)
	print("nao")