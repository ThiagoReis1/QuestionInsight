from math import*
n = int(input("N: "))
cont = 0
sinal = 0
den = 1
num = 1
s = 0
while(cont<n):
	if(cont%2==0):
		sinal = -1
	else:
		sinal = 1
	s = s + (sinal*((num**2)/(7 + den)))
	den = den + 2
	num = num + 1
	cont = cont + 1
print(round(s,11))
	