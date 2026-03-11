from numpy import *

vetor=array(eval(float(input(""))))
i=0
total=0

while (total>75):
	if (total>0):
		total=total+vetor[i]+(i+1)
		i=i+1
	else:
		total=total-vetor[i]+(i+1)
print(total)