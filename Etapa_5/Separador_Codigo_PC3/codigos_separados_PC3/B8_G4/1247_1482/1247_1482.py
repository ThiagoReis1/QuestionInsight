#Thaynara Marques - 21552463
from numpy import*

v = array(eval(input("")))
a = min(v)
b = max(v)
c = 0.75*a + 0.25*b
d = 0.25*a + 0.75*b
x = array(zeros(2,dtype = int))
t = 0
l = 0
for i in range (size(v)):
	if ((v[i]>= a) and (v[i] < c)):
		t = t+1
		x[0] = t
	elif (v[i]>=d) and (v[i]<b):
		l = l+1
		x[1] = l
print (x)
		