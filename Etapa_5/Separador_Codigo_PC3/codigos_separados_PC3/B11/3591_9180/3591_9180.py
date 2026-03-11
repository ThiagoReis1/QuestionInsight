from numpy import*

vetor = array(eval(input('Digite as faces do dado:')))

i = 0
pontos = 0

while i < size(vetor):
	if vetor[i] == 1:
		pontos += 10
		
	if vetor[i] == 2:
		pontos += 5
		
	if vetor[i] == 3:
		pontos += 10
	
	if vetor[i] == 4:
		pontos += 5
		
	if vetor[i] == 5:
		pontos += 10
		
	if vetor[i] == 6:
		pontos += 5
		
	i = i + 1
	
print(pontos)	