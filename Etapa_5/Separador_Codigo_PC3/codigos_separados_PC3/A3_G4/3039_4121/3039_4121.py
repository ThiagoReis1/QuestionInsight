from math import*
x = float(input("Valor: "))
if(x>=-1 and x<-0.5) or (x>0.5 and x<=1):
	y=asin(x)
	y=(degrees(round(x,2)))
else:
	y="entrada invalida"
if(x>=-0.5 and x<=0.5):
	y=acos(x)
	print(degrees(round(x,2)))
else:
	y= "entrada invalida"

	