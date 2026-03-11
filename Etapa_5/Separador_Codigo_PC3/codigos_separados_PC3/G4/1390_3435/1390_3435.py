m = int(input(" Quantos minutos foram usados ? : "))

if	(m <= 100):
	msg = m * 1.20
	
else:
	msg = 25.00 + (m * 1.40)
	
print(round(msg, 2))