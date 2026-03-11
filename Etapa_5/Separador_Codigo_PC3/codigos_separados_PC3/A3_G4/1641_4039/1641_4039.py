from numpy import *
from numpy.int64 import *

vet = array(eval(input()))
q=0
p=0
for elemento in vet:
	if(elemento % 3):
		q=q+1
for elemento in range(0, size(vet)):
	if(vet[elemento] % 3):
		a = vet[elemento](size(vet), dtype=int)
		
print(q)
print(p)