num = int(input("insira o numero:"))

a = num // 1000
b = num % 1000

if (((a - b)**4) == num):
	print(num, "atende a propriedade")
else:
	print((a - b)**4)