from math import*
vc=float(input("qual o valor consumido: "))

if (vc<=300.00):
   gorjeta= (vc *10)/100
else:
   gorjeta= (vc * 6)/100
	
vt= vc + gorjeta

print(round(vt,2))