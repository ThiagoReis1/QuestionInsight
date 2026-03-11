from numpy import*
v = array(eval(input())) 
v = v - 1
for i in range(size(v)):
	if v[i] == -1:
		v[i] = 9
		
print(v)