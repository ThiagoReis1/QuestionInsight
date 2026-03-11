from numpy import*

vetor = (array(eval(input(":"))))
			
j = 0
			
while j < size(vetor):
	if(vetor [j] <= 2):
		vetor[j] = 0
	elif(vetor[j] >= 8):
			vetor[j] = 10
			
	j = j + 1
			
print(vetor)