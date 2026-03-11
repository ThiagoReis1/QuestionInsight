x= input("nome do aminoácido:")
X = x.upper()

if(X=="ARGININA" or X == "TIROSINA" or X == "TRIPTOFANO"):
	if( X == "ARGININA"):
		c = 6
		h =15
		n= 4
		o= 2
		pesom = 12.011*c +1.00794*h + 14.00674*n + 15.9994*o
		print(round(pesom,2))
	elif(X== "TIROSINA"):
		c=9
		h=11
		n=1
		o=3
		pesom = 12.011*c +1.00794*h + 14.00674*n + 15.9994*o
		print(round(pesom,2))
	elif(X == "TRIPTOFANO"):
		c=11
		h=11
		n=2
		o=2
		pesom = 12.011*c +1.00794*h + 14.00674*n + 15.9994*o
		print(round(pesom,2))
else:
	print("Entrada:",x)
	print("Dado Invalido")