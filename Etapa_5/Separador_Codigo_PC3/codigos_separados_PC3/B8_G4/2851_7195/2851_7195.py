from numpy import*
vet=array(eval(input("digite o vetor:")))
r=0

for i in range(size(vet)):
	if vet[i]==99:
		r=r*2
	elif vet[i]!=99:
		r=r+vet[i]
		
print(r)		
		