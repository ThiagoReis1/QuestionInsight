from numpy import *
v = array(eval(input('v:')))
i = 0
for x in range(size(v)):
	if(v[x] <=5):
		i =i + 1		
a = zeros(i, dtype=int)
j = 0
print(i)
for x in range(size(v)):
	if (v[x]<=5):
		a[j] = x
		j = j + 1
		a[j] = x
		
print(a)