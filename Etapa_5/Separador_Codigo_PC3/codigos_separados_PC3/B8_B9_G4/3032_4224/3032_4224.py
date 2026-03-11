x=float(input("x"))

from math import*
if(x<=0):
	tot=0
	print(round(tot,4))
elif((x > 0 )and (x <= 1)):
	tot=1
	print(round(tot,4))
elif((x > 1) and (x <= 2)):
	tot=sqrt(x)
	print(round(tot,4))
elif(x > 2):
	tot=(x**(1/3))
	print(round(tot,4))
