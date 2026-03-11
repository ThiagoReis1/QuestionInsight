from numpy import *
v= array(eval(input("valor do vetor:")))
i=0
while i < len(v):
	if v[i] > 90.00:
		v[i]= v[i] - 6.50
	i= i + 1
print(round(sum(v),2))