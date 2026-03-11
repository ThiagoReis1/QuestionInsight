from numpy import *

v = array(eval(input()))

cont = 0
j = 0

for i in range(size(v)):
	
	if (v[i] >= 5):
		
		cont = cont + 1
		
x = zeros(cont,dtype=int)

for i in range(size(v)):
	if(v[i] >= 5):
		x[j]=i
		j = j + 1
		
print(cont)
print(x)