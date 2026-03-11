peso = float(input("peso da encomenda: "))

if (peso < 4999.9):
	print(peso*0.05)
else:
	print(60+(peso*0.04))