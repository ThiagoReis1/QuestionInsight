from numpy import*
vetor=array(eval(input("Saques: ")))
c=0

for i in vetor:
	if (i<=50):
		c=c+1
print(c)

j=0
vet=arange(0,c)
for i in range(size(vetor)) :
	if vetor[i]<=50:
		vet[j]=i
		j=j+1
print(vet)
	