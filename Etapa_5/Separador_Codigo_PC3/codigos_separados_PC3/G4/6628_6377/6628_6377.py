# faça seu código aqui!
from numpy import*
vet=input().upper()
i=0
j=0
while i<len(vet):
	if vet[i]=="E":
	   j +=1
	i += 1
print(j)	