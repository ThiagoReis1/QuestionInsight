from numpy import *
v = array(eval(input('andares: ')))
i = 0
a = 0
while (i) < size(v):
	if v[i+1] - v[i] < 0:
		a = a + ( v[i] - v[i+1] )
		i = i + 1
	else:
		a = a + ( v[i+1] - v[i] )
		i = i + 1
print(a)
