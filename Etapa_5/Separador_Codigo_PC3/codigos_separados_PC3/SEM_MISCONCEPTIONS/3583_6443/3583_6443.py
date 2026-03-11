from math import * 
vet=array(eval(input()))
for i in range(size(vet)):
 	if vet[i] > 50:
		vet[i]= vet[i] - (0.08 * vet[i])
print(round(sum(vet,2))