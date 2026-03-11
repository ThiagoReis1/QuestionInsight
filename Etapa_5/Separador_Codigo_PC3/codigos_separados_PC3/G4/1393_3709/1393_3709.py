peso = float(input("peso: "))
if (peso <= 4999.9):
	res = peso * 0.05
else:
	res = (peso * 0.04) + 60
print(round(res, 2))