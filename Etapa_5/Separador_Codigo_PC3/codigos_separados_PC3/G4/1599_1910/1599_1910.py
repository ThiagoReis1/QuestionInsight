from numpy import *
v = array(eval(input("")))
a = 0
s = 0.0
while(a<size(v)):
	if(v[a]>80):
		s = s + 0.85*v[a]
	else:
		s = s + v[a]
	a = a + 1
print(round(s,2))
	