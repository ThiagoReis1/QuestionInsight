from numpy import *
v = array(eval(input("Insira o vetor: ")))
for i in range(size(v)):
	if v[i] == 0:
		v[i] = 0
	v[i] = v[i] * 2
print(v)
	
	



