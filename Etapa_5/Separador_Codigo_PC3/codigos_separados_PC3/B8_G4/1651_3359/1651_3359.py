from numpy import*
from numpy.linalg import *

a = input("digite: ").split(',')

v = zeros(6,dtype=int)

for i in range(size(a)):
	if (a[i] == "MC"):
		v[0] = v[0] + 1
	elif (a[i] == "C"):
		v[1] = v[1] + 1
	elif (a[i] == "CM"):
		v[2] = v[2] + 1
	elif (a[i] == "EM"):
		v[3] = v[3] + 1
	elif (a[i] == "E"):
		v[4] = v[4] + 1
	elif (a[i] == "ME"):
		v[5] = v[5] + 1
print(max(v))
print(v)