from math import *
vet=eval(input())
num = 0 
custo = 0 
k = 0 

for i in vet:
	if i < 50:
		vet[i] = vet[i]-(0.08*vet[i])


print(round(sum(vet),2))