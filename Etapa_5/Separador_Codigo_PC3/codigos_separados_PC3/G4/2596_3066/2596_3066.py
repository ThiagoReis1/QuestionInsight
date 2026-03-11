from numpy import *
v = array(eval(input("digite: ")))
k = 0
for i in range(1,size(v)):
	if (v[i] >= v[0]):
		k = k + 1
		print(i)
print(k)
		
	