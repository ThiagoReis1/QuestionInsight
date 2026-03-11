from numpy import *
am = array(eval(input()))
j = 0
for x in am:
	if(x%5==0):
		j = j + 1
print(j)
vr = zeros(j,dtype=int)
i = 0
for x in range(size(am)):
	if(am[x]%5==0):
		vr[i] = x
		i = i + 1
print(vr)
	
	
	

	