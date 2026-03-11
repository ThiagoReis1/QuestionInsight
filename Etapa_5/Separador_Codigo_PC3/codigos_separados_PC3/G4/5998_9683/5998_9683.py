ma = int(input("Quantidades de macas:"))

if ma < 12:
	a = ma * 0.30
	print(round(a,2))
else:
	a = ma * 0.25
	print(round(a,2))