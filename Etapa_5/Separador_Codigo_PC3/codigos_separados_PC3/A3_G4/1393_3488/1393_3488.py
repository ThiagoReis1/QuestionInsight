p = float(input("peso da encomenda: "))

v1 = p * 0.05

v2 = (p * 0.04) + 60.0

if (p <= 4999.9):
	msg = v1

if (p >= 5000.0):
	msg = v2

print(round(msg, 2))