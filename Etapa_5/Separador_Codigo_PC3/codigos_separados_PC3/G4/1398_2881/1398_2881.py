t = int (input("Digite o tempo de voo em minutos: "))

if t<=200:
	c1 = 5000.00 + (100.00 * t)
	print (round(c1,2))

else:
	exc = t - 200
	c2 = (8000.00 + (100*200) + (exc*90))
	print (round(c2,2))

