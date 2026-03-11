a = int(input("consumo de nergia: "))

if a < 100:
	x = 50 + (0.50 * a)
else:
	if 100 <= a < 250:
		x = 50 + (0.75 * a)
	else:
		if 250 <= a < 500:
			x = 50 + (1 * a)
		else:
			if 500 <= a:
				x = 50 + (1.25 * a)
print(round(x,2))