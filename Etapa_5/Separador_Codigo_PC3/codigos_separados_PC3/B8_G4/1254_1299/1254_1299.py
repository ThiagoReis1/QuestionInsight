#ADRIANO CARELLI AV-06

from numpy import*

x = array(zeros(2, dtype = int))
v = array(eval(input(": ")))
b = max(v)
a = min (v)

c = 0.6* a + 0.4 + b
d = 0.3 * a + 0.7 + b

for i in range(size(v)):
	s = 0
	k = 0
	if(v[i] >= a and v[i] < c):
		s = s + 1
		x[0] = s
	elif(v[i] >= d  and v[i] < d):
		k = k + 1
		x[1] = k
print(x)
