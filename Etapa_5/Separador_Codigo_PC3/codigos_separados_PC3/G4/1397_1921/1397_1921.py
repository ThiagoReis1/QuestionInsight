area = float(input("area a ser plantada: "))
if(area <= 10000):
	c = area*5
	print(round(c, 2))
else:
	i = 10000*5
	e = (area - 10000)*4
	t= i + e
	print(round(t,2))