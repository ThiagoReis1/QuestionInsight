a = float (input ("Área:"))

if (a <= 10000):
	v = (a*5)
	print (round (v,2))
else: 
	x = (a - 10000)
	v = (x*4) + 50000
	print (round (v,2))
	
	