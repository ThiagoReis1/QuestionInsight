from numpy import *
v = array(eval(input('v:')))
i = 0
for x in range(size(v)):
	if(v[x] % 5 == 0):
		i += 1		
a = zeros(i, dtype=int)
j = 0
for x in range(size(v)):
	if(v[x] % 5 == 0):
		a[j] = x
		j += 1
print(i)
print(a)

	
		

			 
			 
			 