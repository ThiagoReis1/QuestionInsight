valor = int(input("valor: "))
x = valor % 29
y = valor // 29


if x == 0:
	print(y)
	print("sim")

else:
	print(x)
	print("nao")
