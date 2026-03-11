t = float(input("tempo de voo: "))

x = (5000 + (100 * t))
z = (8000 + (100 * t) + 90 * (t > 200))

if (t <= 200):
	msg = x
else:
	msg = z
	
print(round(msg, 2))