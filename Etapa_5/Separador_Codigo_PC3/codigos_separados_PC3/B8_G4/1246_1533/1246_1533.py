from numpy import*
v = array(eval(input("")))
a = min(v)
b = max(v)	 
c = 0.75 * a + 0.25 * b
d = 0.25 * a + 0.75 * b
z = array(zeros(2, dtype = int))
for i in range(size(v)):
	if (v[i]>= a and v[i] < c):
			 z[0] = z[0] +1
	elif (v[i] >= c and v[i]< d):
			 z[1] = z[1] +1
print(z)