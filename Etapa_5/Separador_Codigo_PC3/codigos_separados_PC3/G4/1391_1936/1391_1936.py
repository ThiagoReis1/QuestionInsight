n = float(input("consumo de energia:\n"))
if (n<=150):
	a = (n*0.6)+5
	print(round(a,2))
else:
	a = (n*0.75)+16
	print(round(a,2))