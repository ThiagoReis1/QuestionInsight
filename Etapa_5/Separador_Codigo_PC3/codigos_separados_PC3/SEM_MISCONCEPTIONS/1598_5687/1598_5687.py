from numpy import *

vetor = array(eval(input("")))
total = 0
i = 0 

while(i<size(vetor)):
	if(vetor[i] > 90):
		total = total + vetor[i] - 6.5
	else:
		total = total + vetor[i]
	i = i + 1
print(round(total,2))


