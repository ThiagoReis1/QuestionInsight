from numpy import*
from math import*
vet = array(eval(input("valor")))
k =0
for i in range(0,size(vet)):
	k = k +exp(vet[i])
d = k/exp(size(vet))
m=log(d)

print(round(m,2))