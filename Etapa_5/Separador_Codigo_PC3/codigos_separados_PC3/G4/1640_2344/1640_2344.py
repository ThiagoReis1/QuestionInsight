from numpy import *

vet= array(eval(input("Digite um vetor:")))

cont= 0

for i in vet:
	if(i % 2 != 0):
		cont= cont + 1

n= zeros(cont,dtype= int)

nova_cont= 0

for i in range(size(vet)):
	if(vet[i] % 2 != 0):
		n[nova_cont]= i
		nova_cont= nova_cont + 1
		
print(cont)		
print(n)