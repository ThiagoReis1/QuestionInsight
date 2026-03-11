num = int(input("Insira numero: "))
div = num // 41
res = num % 41
if (num % 41 == 0):
	print(div)
	print("sim")
else:
	print(res)
	print("nao")