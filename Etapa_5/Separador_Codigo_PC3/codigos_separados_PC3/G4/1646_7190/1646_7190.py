from numpy import *

v = array(eval(input(":")))
s = 0
i = 0
for i in range(size(v)):
	if(v[i]<=50):
		i = i+1
		s = s+1
print(s)

n = zeros(s,dtype=int)
k = 0
j = 0

for i in v:
	if(v[j]<=50):
		n[k]= j
		k = k+1
		j = j+1
	else:
		j=j+1
print(n)
	
	


