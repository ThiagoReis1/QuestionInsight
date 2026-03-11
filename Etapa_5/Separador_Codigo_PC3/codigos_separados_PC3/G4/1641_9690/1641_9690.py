from numpy import *

v = array(eval(input("v: ")))
k = 0

for i in range(size(v)):
	if v[i]%3==0:
		k+=1
print(k)

aux = zeros(k,dtype=int)
j=0
for i in range(size(v)):
	if v[i]%3==0:
		aux[j]=i
		j+=1
print(aux)