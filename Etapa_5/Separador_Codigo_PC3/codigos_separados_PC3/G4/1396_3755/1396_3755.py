v=float(input('valor:'))
if(v<=300):
	x=v+(v*(10/100))
	print(round(x,2))
else:
	x=v+(v*(6/100))
	print(round(x,2))