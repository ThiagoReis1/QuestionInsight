x=int(input("Digite um numero divisivel por 19: "))

if x % 19 == 0:
	print(x//19)
	print("sim")
else:
	print(x%19)
	print("nao")
