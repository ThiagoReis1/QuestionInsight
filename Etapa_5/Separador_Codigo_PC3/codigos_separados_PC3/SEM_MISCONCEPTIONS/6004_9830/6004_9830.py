a = int(input("digite a quantidade de tomates: "))

if a >= 4:
	total = a * 0.55
	print(round(total, 2))
else: 
	total = a * 0.75
	print(round(total, 2))