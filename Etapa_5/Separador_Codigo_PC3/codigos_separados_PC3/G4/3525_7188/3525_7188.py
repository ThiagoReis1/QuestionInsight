from math import*
nx= float(input("numero real"))
nk= int(input("numero inteiro"))
e=0
cont=0
while cont< nk:
	f= factorial(2*cont+1)
	e= e+ (nx**(2*cont+1)/f) 
	cont= cont + 1
print(round(e,9))