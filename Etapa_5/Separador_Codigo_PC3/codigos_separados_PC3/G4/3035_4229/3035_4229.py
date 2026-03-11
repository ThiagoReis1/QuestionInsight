from math import*
x=(float(input("")))
if(x>=0) and (x<90) or (x>=180) and (x<270):
	z=radians(x)
	y=sin(z)
	print(round(y,4))
elif(x>=90) and (x<180) or (x>=270) and (x<360):
	z=radians(x)
	y=cos(z)
	print(round(y,4))
else:
	print("entrada invalida")
	