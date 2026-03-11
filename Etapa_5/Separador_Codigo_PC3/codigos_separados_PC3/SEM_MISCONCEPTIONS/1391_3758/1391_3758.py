energia = int(input("consumo de energia: "))
if(150>=energia):
	total = (energia * 0.60 + 5)
	print(round(total , 2))
else:
	total = energia * 0.75 + 16
	print(round(total,2))