from numpy import *
v=array(eval(input("digite distancia")))
i=0
j=0
r=98.48
print(r)
while i<size(v):
	if v[i]<r:	
		j=j+1		
	i=i+1
print(j)	