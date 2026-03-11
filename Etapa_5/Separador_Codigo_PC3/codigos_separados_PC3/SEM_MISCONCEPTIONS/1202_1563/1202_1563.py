from numpy import*
v = array(eval(input("temp: ")))
s = size(v)
x = 0
n = 0
while (s > 0):
	if (v[0 + x] < 23):
		n =  n + 1
	x = x + 1
	s = s - 1	
print (n)
while ()