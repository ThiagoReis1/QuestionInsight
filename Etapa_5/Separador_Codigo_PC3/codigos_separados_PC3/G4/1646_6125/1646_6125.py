from numpy import *
v= array(eval(input("")))

j=0
baixo= 0
for i in range(size(v)):
	if v[i] <= 50:
		baixo = baixo + 1
p = zeros(baixo, dtype= int)
for i in range(size(v)):
	if v[i] <= 50:
		p[j]=i
		j=j+1
	
	

		
print(baixo)		
print(p)