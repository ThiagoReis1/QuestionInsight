from numpy import *

v = array(eval(input("valor do vetor: ")))

n = size(v)
soma = 0

for i in range(n):
	if(v[i] > v[0]):
	   print(i)
		
	if(v[i] > v[0]):
		soma = soma + 1

print(soma)
	