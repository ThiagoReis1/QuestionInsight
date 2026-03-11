from numpy import*

vet = array(eval(input("vetor: ")))
 
for i in range(size(vet)):
	if(vet[0]> vet[i]):
		cont_via = cont_via + 1
	print(vet[i])

	print(cont_via)
