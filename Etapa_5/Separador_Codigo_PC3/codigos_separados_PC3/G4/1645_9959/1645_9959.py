from numpy import *

x = array(eval(input()))
c = 0

for i in range (size(x)):
	if x[i] >= 2000:
		c+=1
		
k = zeros(c, dtype=int)
print(c)

j = 0

for i in range (size(x)):
	if x[i] >= 2000:
		k[j] = i
		j+=1
print(k) 