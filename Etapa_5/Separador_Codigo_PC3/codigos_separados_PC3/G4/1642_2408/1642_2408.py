from numpy import *
 
v = array(eval(input()))
x = 0

for i in range(size(v)):
	if(v[i]%5==0):
		x = x + 1	
print(x)	

s = zeros(x, dtype=int)
j = 0
for i in range(size(v)):
	if(v[i]%5==0):
		s[j] = i
		j = j + 1
print(s)