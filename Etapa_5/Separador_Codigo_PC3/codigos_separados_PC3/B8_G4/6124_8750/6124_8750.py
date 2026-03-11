p = float(input("peso do tripulante: "))

if (p >= 3000.0) and (p < 3400.0):
	z = 0.8*p
	print(round(z, 1))
elif (p >= 3400.0) and (p < 3900.0):
	z = 1.3*p
	print(round(z, 1))
elif (p >= 3900.0) and (p < 4100.0):
	z = 2.1*p
	print(round(z, 1))
elif (p >= 4100.0):
	z = 3.0*p
	print(round(z, 1))