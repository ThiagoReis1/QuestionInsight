from numpy import *

v = array(eval(input("digite o vetor: ")))


i = 0
soma = 0

for i in range(size(v)):
	soma = soma + v[i]
	
i = 0
soma2 = 0

for i in range(size(v)):
	if(v[i] >= 80):
		soma2 = soma2 + (v[i]*0.85)

i = 0
soma3 = 0

for i in range(size(v)):
	if(v[i] >= 80):
		soma3 = soma3 + v[i]

ct = (soma - soma3) + soma2

print(round(ct,2))
		