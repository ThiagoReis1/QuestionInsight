from numpy import *
v = array(eval(input()))

cont = 0
for i in range(1,size(v)):
	if v[i] > (v[0] * 1.5):
		print(i)
		cont+=1
print(cont)