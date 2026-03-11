a = float(input("valor consumido:"))

if	(a<=300):
	b = 10/100
	c = a+(a*b)
else:
	b = 6/100
	c = a+(a*b)
	
print(round(c, 2))