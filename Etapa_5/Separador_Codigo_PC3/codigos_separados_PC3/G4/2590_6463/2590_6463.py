from numpy import *

v = array(eval(input("valor: ")))

i = 1
ind = 0
while i < size(v):
	if v[i] < v[0]:
		ind = ind + 1
		print(i)
	i = i + 1
print(ind)