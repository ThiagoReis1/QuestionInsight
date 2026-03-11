from numpy import*
caracteres = input("Digite uma letra:")
vetor = zeros(4, dtype = int)

for i in range(len(caracteres)):
	if caracteres[i] == 'A':
		vetor[0] = vetor[0] + 1
	elif caracteres[i] == 'B':
		vetor[1] = vetor[1] + 1
	elif caracteres[i] == 'C':
		vetor[2] = vetor[2] + 1
	elif caracteres[i] == 'D':
		vetor[3] = vetor[3] + 1
		
print(vetor)
	
	
