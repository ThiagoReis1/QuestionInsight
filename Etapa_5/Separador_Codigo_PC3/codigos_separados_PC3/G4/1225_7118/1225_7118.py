from numpy import*
from math import*

vet = array(eval(input()))
n = size(vet)
m = sum(vet)/size(vet)
a = 0

for i in range(size(vet)):
	a = a + (vet[i] - m) ** 2
	
d = sqrt(a/(n - 1))
print(round(d, 3))