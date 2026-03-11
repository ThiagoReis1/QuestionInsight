# entrada de um numero inteiro x
x = int(input("digite o valor de x"))


if x % 31 == 0: 
	print(round(x // 31))
	print("sim")

else: 
	print(round(x % 31))
	print("nao")