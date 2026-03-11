from numpy import *

vet = array(eval(input("Digite o vetor: ")))
v = 0
for i in vet:
	if (i <= 50):
		v = v + 1
		
x = zeros(v, dtype = int)
count = 0
for j in range(size(vet)):
	
	if (vet[j] <= 50):
		x[count] = j
		count += 1
		
print(count)
print(x)