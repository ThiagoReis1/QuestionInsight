p = float(input("peso dos tripulantes: "))

if (p >= 3000)and(p < 3400):
	z = p * 0.8
elif (p >= 3400)and(p < 3900):
	z = p * 1.3
elif (p >= 3900)and(p < 4100):
	z = p * 2.1
elif (p >= 4100):
	z = p * 3
print(round(z, 2))