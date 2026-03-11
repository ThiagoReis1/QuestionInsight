from numpy import *
v = array(eval(input("")))
n = int(input(""))
c = 0
s = size(v)
for i in range(s):
	if v[i] == n:
		print(i)
for i in range(s):
	if v[i] > n:
		c = c+1
print(c)