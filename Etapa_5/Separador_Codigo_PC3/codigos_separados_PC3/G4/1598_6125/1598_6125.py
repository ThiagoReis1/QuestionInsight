from numpy import *
v= array(eval(input()))
i=0
d=0
while i < size(v):
	if v[i] > 90:
		d= d + 6.50
	i=i+1
		
print(round(sum(v)-d ,2))
		

