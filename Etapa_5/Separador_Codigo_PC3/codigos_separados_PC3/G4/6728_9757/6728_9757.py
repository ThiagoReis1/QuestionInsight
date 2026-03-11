x = int(input("Digite um numero: "))
y = 37
a = x%y
if a == 0:
	print(x//y)
	print("sim")
else:
	print(a)
	print("nao")