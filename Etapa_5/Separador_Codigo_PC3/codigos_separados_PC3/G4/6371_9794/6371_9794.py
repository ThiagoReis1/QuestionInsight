from numpy import *
v = array(eval(input("insira o numero: ")))
for i in range(size(v)):
	if v[i] == 0:
		v[i] = 81
	else:
		v[i] = (v[i]-1)**2
print(v)