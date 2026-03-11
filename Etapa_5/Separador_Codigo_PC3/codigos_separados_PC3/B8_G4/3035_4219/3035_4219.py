from math import *
x = float(input("insira: "))
if (0>x) or (x>360) :
	print ("entrada invalida")
else :
	if (0<=x) and (x<90) or (180<=x) and (x<270):
		c = radians(x)
		b = sin (c)
		print (round(b, 4))
	elif (90<=x) and (x<180) or (270<=x) and (x<360):
		d = radians (x)
		a = cos (d)
		print (round(a, 4))