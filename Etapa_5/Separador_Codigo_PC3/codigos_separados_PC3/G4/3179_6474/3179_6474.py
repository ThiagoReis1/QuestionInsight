from numpy import*

vet = array(eval(input("Digite um vetor de numeros: ")))

n = zeros(size(vet), dtype = int)
j = 0

for i in range(size(vet)) :
	
	if vet[i] != 1 :
		
		n[j] = vet[i]
		j = j + 1
		
while j < size(n) :
	
	if n[j] == 0 :
		
		n[j] = 1
	
	j = j + 1
print(n)