num = int(input("Digite um numero: "))

if (num % 1000 - num // 1000)**2:
	total = ((num % 1000 - num // 1000)**2)
	print(total)
else:
	total = (num % 1000)**2 - (num // 1000)**2
	print(total)