from numpy import*

vetor = array(eval(input('area: ')))

i = 0
p = 100

while i < size(vetor):
	
	if vetor[i] == 1:
		p = p * 5
	if vetor[i] == 2:
		p = p * 3
	if vetor[i] == 3:
		p = p
	if vetor [i] == 4:
		p = p/2
	i+=1
print(round(p,2))