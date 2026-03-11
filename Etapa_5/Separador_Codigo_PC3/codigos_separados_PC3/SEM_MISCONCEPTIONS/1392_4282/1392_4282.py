entrada = float(input())

if (entrada < 10.0):
	total = 30.0 + (3.0 * entrada)
else:
	total = 30.0 + (3.5 * entrada)
print(round(total, 2))