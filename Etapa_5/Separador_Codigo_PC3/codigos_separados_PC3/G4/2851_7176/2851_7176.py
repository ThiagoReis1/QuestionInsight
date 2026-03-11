from numpy import*
vet=array(eval(input("vetor:")))
soma=0
for i in range(size(vet)):
	if(vet[i]!=99):
		soma=soma+vet[i]
	else:
		soma=soma*2
print(soma)