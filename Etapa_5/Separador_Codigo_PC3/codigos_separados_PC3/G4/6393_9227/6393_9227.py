from numpy import*
v = array(eval(input("")))
for i in range(size(v)):
	if v[i] == 9:
		v[i] = 0
		
	else:
		v[i] += 1
		
print(v**3)