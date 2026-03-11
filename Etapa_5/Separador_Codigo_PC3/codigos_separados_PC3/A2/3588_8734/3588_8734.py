from numpy import*

vetor = array(eval(input('faio')))

i = 0
p = 10000

while i < size(vetor):
	if vetor[i] == 1:
		p = p * 2
	
	if vetor[i] == 2:
		p = p 
	
	if vetor[i] == 3:
		p = p / 2 
	
	if vetor[i] == 4:
		p = p / 4
	
	i += 1
print(round(p,2))