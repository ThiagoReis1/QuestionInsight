from numpy import *

caixa=array(eval(input("saques: ")))

soma= 0
j=0

for i in range(size(caixa)):
	if caixa[i] >= 2000:
		soma= soma + 1
print(soma)
vet=zeros(soma,dtype=int)
for i  in range(size(caixa)):
	if caixa[i] >= 2000:
		vet[j]= i
		j = j + 1

print(vet)
	