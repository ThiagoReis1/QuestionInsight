from numpy import *
v = array(eval(input("tempo de cada corredor: ")))
a = size(v)
for i in range(a):
	if v[i] == max(v):
		print(i)