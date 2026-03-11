quan = int(input("Insira a quantidade de tomates: "))
if quan >= 4:
	total = quan*0.55
	print(round(total, 2))
else:
	total = quan*0.75
	print(round(total, 2))