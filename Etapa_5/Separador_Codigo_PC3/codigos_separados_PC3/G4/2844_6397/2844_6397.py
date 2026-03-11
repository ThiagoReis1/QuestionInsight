from numpy import*
v = array(eval(input(":")))

for i in range(size(v)):
	if (v[i] > 0):
		v[i] = v[i] - 1 
	else:
		v[i] = 9
		
print(v)