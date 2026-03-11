v = float(input("valor de vendas "))

if (v < 1000):
	g = ((v*5)/100)
	print(round(g,2))	 
else:
	c =(v-1000)
	l =((c*10)/100)
	p =(50+l)	 
	print(round(p,2))


