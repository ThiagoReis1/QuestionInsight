x = int(input("insira um numero inteiro: "))

if x%19 == 0:
	print(x//19)
	print("sim")
else:
	print(x%19)
	print("nao")