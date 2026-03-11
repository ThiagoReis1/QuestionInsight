from numpy import *

v =eval(input("Vetor: "))
cont=0

for x in range(size(v)):
	if v[x]<=-3:
		cont=cont+1
		print(x)
print(cont)