from numpy import*

a = array(eval(input()))

v = zeros(size(a), dtype = int)

for i in range(size(a)):
	
	if(a[i] == 0):
		v[i] = 9
	else:
		v[i] = a[i]-1
		
print(v)