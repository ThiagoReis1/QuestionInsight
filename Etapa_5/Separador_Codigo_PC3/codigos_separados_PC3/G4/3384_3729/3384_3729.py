u = input("digite o ou k: ")
m = float(input("medida: "))
if (u.upper() == "O"):
	r = m / 35.274
else:
	r = 35.274 * m
print(round(r,2))