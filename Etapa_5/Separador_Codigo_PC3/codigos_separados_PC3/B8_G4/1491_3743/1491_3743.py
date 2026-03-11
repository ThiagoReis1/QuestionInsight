peso = float(input())
if peso >= 0 and peso <= 5000:
	print(round(peso * 0.03 + 20,2))
elif peso >= 5001 and peso <= 6000:
	print(round(peso * 0.04 + 25,2))
elif peso >= 6001 and peso <= 7000:
	print(round(peso * 0.05 + 30,2))
elif peso >= 7000:
	print(round(peso * 0.06 + 35,2))