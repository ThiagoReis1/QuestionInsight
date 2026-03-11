a = float(input("vendas: "))

if(a <= 1000):
	print(round(a * 5 / 100, 2))

else:
	print(round((a * 5/100) + ((a - 1000) * 5/100), 2))