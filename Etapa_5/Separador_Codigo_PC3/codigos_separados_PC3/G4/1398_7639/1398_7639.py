a = float(input("tempo de voo: "))

if (a<=200):
	b = 5000+(100*a)
	print(round(b,2))
else:
	c = (a-200)
	d = 8000+(100*200)+(90*c)
	print(round(d,2))
	
	