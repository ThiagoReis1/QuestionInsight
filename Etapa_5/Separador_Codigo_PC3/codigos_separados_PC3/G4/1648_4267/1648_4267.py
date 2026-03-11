from numpy import *
vet = array(eval(input("Digite o vetor: ")))
rep = 0
p = size(vet)
j = 0
k = 0
repi = zeros(p,dtype=int)
for i in range (size(vet)):
	if (vet[i]<70):
		rep = rep + 1		
for i in range (size(vet)):	
	if(vet[i]<70):
		repi[j] = i
		j = j + 1
resp = zeros(rep,dtype=int)
for i in range (size(repi)):
	if(repi[i]>0):
		resp[k]=repi[i]
		k = k + 1
print(rep)			
print(resp)
