from numpy import *
from math import *

v= array(eval(input("Numero de alunos:")))
n=0 

for x in v:
	if x%2==0:
		n=n+1
print (n)

z= zeros(n, dtype=int)

i=0
p=0

for i in range(size(v)):
	if v[i]%2==0:
		z[p]=i
		i=i+1
		p=p+1
	else:
		i=i+1
		
print(z)