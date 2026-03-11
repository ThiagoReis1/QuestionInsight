from math import*
from numpy import*

v= array(eval(input('vetor: ')))

cont=0
for i in range(size(v)):
	if v[i]<=50:
		cont=cont+1
print(cont)

u= zeros(cont,dtype=int)
j=0
for i in range(size(v)):
	if v[i]<=50:
		u[j]=i
		j=j+1
print(u)