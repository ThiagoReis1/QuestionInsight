t = float(input("Tempo de voo: "))
if (t <= 200):
	c = t*100 + 5000
	print(round(c,2))
else:
	ca = 200*100 + (t-200)*90 + 8000
	print(round(ca,2))