# Phillip de Sousa Silva 
# av 04,Ex 02
# 26/07/2016

from math import*

x = int(input("X:"))
cont = 1
j=1
k=1
t=0
while  x > 0:
	if cont%2==0:
		t = t - (j**3)/(5+(k))
	else:
		t = t + (j**3)/(5+(k))
	
	cont = cont + 1
	x = x-1 
	j = j+1
	k = k+2

print(round(t,9))