c = float(input("consumo= "))

if c >= 10:
	t = 3.5
else:
	t = 3.0

V = 30 + t*c

print(V)