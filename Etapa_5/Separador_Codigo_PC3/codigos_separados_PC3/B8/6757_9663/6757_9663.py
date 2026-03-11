p = int(input("Digite a quantidade desejada: "))

if p < 3:
	total = p * 5 + 3
	print(round(total,2))
elif p == 3:
	total = p * 5 + 3.25
	print(round(total,2))
elif p > 3:
	total = p * 5 + 4.50
	print(round(total,2))