t= float(input("tempo de voo: "))

if(t<=200):
	c= 5000+ 100*t
	print(round(c, 2))
else:
	c=8000+ 100*200 +90*(t-200)
	print(round(c, 2))