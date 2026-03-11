from numpy import *

v = input(":").upper()
v1 = zeros(len(v),dtype=float)
i = 0
c= 0

while(i<len(v)):
	
	if(v[i]== "A" or v[i]=="E" or v[i]=="I" or v[i]=="O" or v[i]=="U"):
		v1[i]= 0.19

	else:
		v1[i]= 0.23

	i = i+1
	
print(round(sum(v1),2))
