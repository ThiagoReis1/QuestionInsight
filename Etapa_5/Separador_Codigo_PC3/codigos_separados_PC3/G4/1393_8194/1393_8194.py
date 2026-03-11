g = float(input("peso: "))

if (g < 5000):
	cont = g * 0.05
else:
	cont = g * 0.04 +60
print(round(cont, 2 ))