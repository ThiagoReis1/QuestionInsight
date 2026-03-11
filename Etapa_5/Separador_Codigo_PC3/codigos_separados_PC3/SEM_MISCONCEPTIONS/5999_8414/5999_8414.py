qt = int(input("Qual a quantidade: "))

if qt < 6:
	total = round(qt * 0.75, 2)
	print(total)
else:
	total = round(qt * 0.60,2)
	print(total)
