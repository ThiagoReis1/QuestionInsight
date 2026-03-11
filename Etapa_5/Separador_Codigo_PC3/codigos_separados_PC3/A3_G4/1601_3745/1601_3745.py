from numpy import*
vet = array(eval(input("Digite o vetor: ")))
t = min(vet)
i = 0
j = 0
while(i < size(vet)):
	if(vet[i] == t):
		j = i
	i = i + 1
print(j)	
