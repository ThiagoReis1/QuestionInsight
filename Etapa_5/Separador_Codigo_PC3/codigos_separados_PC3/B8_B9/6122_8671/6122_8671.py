comb = float(input("comb: "))

if (comb <= 17.5):
	total = comb + 0.8
	print(round(total, 1))
elif (comb > 17.5) and (comb <= 35.0):
	total = comb + 1.3
	print(round(total, 1))
elif (comb > 35.0) and (comb <= 50):
	total = comb + 2.1
	print(round(total, 1))
elif (comb > 50):
	total = comb + 3.0
	print(round(total, 1))