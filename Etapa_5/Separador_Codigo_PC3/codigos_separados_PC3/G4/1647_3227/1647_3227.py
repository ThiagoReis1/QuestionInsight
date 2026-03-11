from numpy import *

vet = array(eval(input("Digite: ")))
v = 0

for i in vet:
	if(i >= 70):
		v += 1
		
x = zeros(v, dtype=int)
v = 0
for j in range(size(vet)):
	if (vet[j] >= 70):
		x[v] = j
		v +=  1

print(v)
print(x)