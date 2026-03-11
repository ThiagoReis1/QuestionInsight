from numpy import *
v = array(eval(input("v:")))
v2 = array(eval(input("v2")))
a = 0
v3 = v + v2

for y in v3:
	if(y >= 12):
		a = a + 1
print(v3)
print(a)