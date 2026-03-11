from numpy import*

vet = array(eval(input("vetor: ")))
l = 0
soma = 0
for i in range(size(vet)):
	soma = soma + vet[i]
	if(vet[i] >= 5):
		l = l + 1
		
print(soma)
print(l)
		
		
	