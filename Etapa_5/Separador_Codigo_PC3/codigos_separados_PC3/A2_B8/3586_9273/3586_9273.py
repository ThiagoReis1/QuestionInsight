from numpy import*

vetor = array(eval(input(" ")))
inicio = 0
i = 0
total = inicio 

while i < len(vetor):
	if vetor[i] == 1:
		total = total + 100
	elif vetor[i] == 2:
		total = total + 60
	elif vetor[i] == 3:
		total = total + 20
	elif vetor[i] == 4:
		total = total 
	i = i + 1
print(total)
