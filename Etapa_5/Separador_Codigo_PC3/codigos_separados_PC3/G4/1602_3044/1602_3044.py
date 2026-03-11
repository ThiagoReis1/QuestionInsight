from numpy import*
vet=array(eval(input("vetor: ")))
for i in range(size(vet)):
	if(vet[i]==max(vet)):
		print(i)