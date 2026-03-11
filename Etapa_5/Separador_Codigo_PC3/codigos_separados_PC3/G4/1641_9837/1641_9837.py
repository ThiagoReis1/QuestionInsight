from numpy import *
v = array(eval(input("insira um:")))
k = 0
for k in range(size (v)):
	if v%3 == 0:
		k+=1
	print(k)
aux =zeros(k, dtype=int)
for m in range(size(v)):
	if v[m]%3 == 0:
		aux[m]=1
		m+=1
	print(aux)
