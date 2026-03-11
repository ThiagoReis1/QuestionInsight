from numpy import *

vetor = array(eval(input()))

i = 0
j = 0

while i < size(vetor):
	if vetor[i] == 1:
		j = j + 10
	elif vetor[i] == 2:
		j = j + 5
	elif vetor[i] == 3:
		j = j
	elif vetor[i] == 4:
		j = j + 5
	elif vetor[i] == 5:
		j = j + 20
	elif vetor[i] == 6:
		j = j + 10
	i += 1
print(j)