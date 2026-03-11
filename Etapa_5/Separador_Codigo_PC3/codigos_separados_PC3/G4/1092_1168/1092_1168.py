num = int(input("numero: "))
cent = num // 100
dez = (num % 100) // 10
unid = num % 10
if (num == (cent ** 3) + (dez ** 3) + (unid ** 3)):
	print(num, "atende a propriedade")
else:
	print((cent ** 3) + (dez ** 3) + (unid ** 3))
	
		