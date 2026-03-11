a = float(input("Quantidade de combustivel comum: "))

if a > 0 :
	if a < 17.5 :
		r = a + 1.5
		print(round(r, 1))
	elif 17.5 <= a < 35 :
		r = a + 2.3
		print(round(r, 1))
	elif 35 <= a < 50 :
		r = a + 3.3
		print(round(r, 1))
	else:
		r = a + 4.7
		print(round(r, 1))