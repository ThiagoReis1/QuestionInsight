from numpy import*
vet = array(eval(input("Digite o vetor: ")))
vcont= zeros(3, dtype=int)
for i in range(0, size(vet)):
	if(vet[i]%2 == 0):
		vcont = vcont 
print(vcont)