num = int(input("digite o numero de tomates comprados: "))
if num>=4:
	total = num*0.55
	print(round(total,2))
else:
	total = num*0.75
	print(round(total,2))