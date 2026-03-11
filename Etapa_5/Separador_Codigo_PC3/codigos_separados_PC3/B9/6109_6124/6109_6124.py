comb = float(input("Quantidade de combustivl comum: "))

if comb < 17.5:
	total = comb + 1.5
	print(round(total, 1))
elif comb >= 17.5 and comb <= 35.0:
	total = comb + 2.3
	print(round(total, 1))
elif comb >= 35.0 and comb <= 50.0:
	total = comb + 3.3
	print(round(total, 1))
else:
	comb >= 50.0
	total = comb + 4.7
	print(round(total, 1))