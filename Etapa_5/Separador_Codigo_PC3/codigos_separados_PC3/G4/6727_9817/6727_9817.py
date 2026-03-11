x= int(input("Digite um numero inteiro:"))

if x % 31 == 0:
	print(x//31)
	print("sim")
else:
	print(x % 31)
	print("nao")