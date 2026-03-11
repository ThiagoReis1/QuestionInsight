from numpy import*

vetor = array(eval(input("Digite o vetor de notas: ")))

i = 0

while i < size(vetor) :
	
	if vetor[i] > 4 and vetor[i] < 5 :
		
		vetor[i] = 4
		
	elif vetor[i] > 9 and vetor[i] < 10 :
		
		vetor[i] = 10
		
	else :
		
		vetor[i] = vetor[i]
		
	i = i + 1

print(vetor)