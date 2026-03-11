from numpy import*
from math import*
v= array(eval(input()))
p=0

for i in range(0,size(v)):
	p= p + exp(v[i])
	
j= p /exp(size(v))
m= log(j)

print(round(m,2))
		  
		  