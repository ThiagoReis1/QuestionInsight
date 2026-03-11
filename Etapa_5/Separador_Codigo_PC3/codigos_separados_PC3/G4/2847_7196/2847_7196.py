from numpy import*

v = array(eval(input(" ")))

for i in range(size(v)):
	if v[i] >= 0 and v[i] <= 9:
		v[i] = v[i]**2
print(v)