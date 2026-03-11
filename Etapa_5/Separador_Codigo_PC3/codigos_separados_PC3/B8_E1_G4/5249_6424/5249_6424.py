p = int(input())
s = int(input())
b = int(input())

if p <= 0 and p > 4 and s <= 0 and s > 4 and b <= 0 and b > 4:
	print("")
else:
	t = x + y + z
	if 1 <= p <= 4 :
		if p == 1:
			x = 180
		elif p == 2:
			x = 230
		elif p == 3:
			x = 250
		elif p == 4:
			x = 350

	elif 1 <= s <= 4:		
		if s == 1:
			y = 75
		elif s == 2:
			y = 110
		elif s == 3:
			y = 170
		elif s == 4:
			y = 200

	elif 1 <= b <= 4:
		if b == 1:
			z = 20
		elif b == 2:
			z = 70
		elif b == 3:
			z = 100
		elif b == 4:
			z = 65
	print("Entradas: {} , {} , {}".format(p,s,b))
	print("Calorias: {} cal".format(t))

