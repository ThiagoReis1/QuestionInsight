from numpy import *
v = array(eval(input('v:')))
i = 0
for x in range(size(v)):
	if(v[x] <=50):
		i += 1		
a = zeros(i, dtype=int)
j=0
for x in range(size(v)):
	if(v[x] <=50):
		v[x] = j
		j=j+1
print(i)
print(x)