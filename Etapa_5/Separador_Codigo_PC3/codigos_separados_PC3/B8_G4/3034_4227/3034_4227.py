x = float(input(""))
from math import*
if (x<-4)or(x>4):
	print("entrada invalida")
elif (x>=-4 and x<0):
	print(round(abs(x)**(1/2),4))
elif (x==0):
	print(round(0,4))
elif ((x>0)and(x<=4)):
	print(round(x**(1/2),4))