from numpy import *

vet= array(eval(input("digite vetor: ")))

result = 0


for i in range(size(vet)):
	if(vet[i] <= 50):
		result = result + 1
print(result)
c= zeros(result, dtype=int)
s=0
for i in range(size(vet)):
	if(vet[i]<=50):
		c[s]=i
		s=s+1
print(c)		
		
