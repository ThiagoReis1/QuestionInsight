from numpy import*

vet= array(eval(input()))

cont=0
for i in vet:
	if(i%2 == 0):
		cont= cont + 1
		
vetor= zeros(cont,dtype=int)

j=0
for i in range(0,size(vet)):
	if(vet[i]%2 == 0):
		vetor[j]=i
		j= j+1
	i=i+1

print(cont)
print(vetor)
