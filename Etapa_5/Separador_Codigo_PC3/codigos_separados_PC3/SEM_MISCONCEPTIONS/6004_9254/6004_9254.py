num = int(input("numero de tomates: "))

if num < 4:
	valor = num * 0.75
	print(round(valor, 2))
else:
	valor = num * 0.55
	print(round(valor, 2))