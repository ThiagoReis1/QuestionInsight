from numpy import *
from math import *

vet = array(eval(input()))
n = size(vet)
m = sum(vet)/size(vet)
b = 0

for i in range(size(vet)):
	b = b + (vet[i]-m)**2
	
d = sqrt(b/(n-1))
print(round(d,3))

