#coloque em minutos
t = float(input("tempo de voo: "))
if(t<=200):
	c = (100 * t) + 5000
	print(round(c, 2))
else:
	e = (t - 200)
	d = (100 * 200) + (e * 90) + 8000
	print(round(d, 2))
