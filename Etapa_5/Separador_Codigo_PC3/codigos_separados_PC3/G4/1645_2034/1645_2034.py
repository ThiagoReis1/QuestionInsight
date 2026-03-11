from numpy import*
saque= array(eval(input("saque:"))) 
qtd=0
for i in range(size(saque)):
	if(saque[i]>=2000):
		qtd=qtd + 1

vet2= zeros(qtd, dtype=int)
x=0
for j in range(size(saque)):
	if(saque[j]>=2000):
		vet2[x]=j
		x=x+1
print(qtd)		
print(vet2)		


