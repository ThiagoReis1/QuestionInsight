from numpy import *
vet= array(eval(input("digite os saques: ")))
c=0
u=0
for i in range(size(vet)):
	if(vet[i] <= 50):
		c= c + 1
print(c)
cont= zeros(c, dtype=int)
for i in range(size(vet)):
	if(vet[i] <= 50):
		cont[u]= i
		u= u+1
print(cont)