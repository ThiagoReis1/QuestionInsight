from numpy import*
vet=array(eval(input("vetor:")))
s=0
for i in range(size(vet)):
	s=s+exp(vet[i])
z=s/exp(size(vet))
print(round(log(z),2))