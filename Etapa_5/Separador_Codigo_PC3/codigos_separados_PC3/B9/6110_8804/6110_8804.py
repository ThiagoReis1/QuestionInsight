comb = float(input("quant de combustivel comum: "))
if comb < 17.5:
	total = comb + 10.5
elif comb >= 17.5 and comb <= 35.0:
	total = comb + 14.0
elif comb >= 35.0 and comb <= 50.0:
	total = comb + 18.6
else:
	total = comb + 24.5
print(round(total, 1))