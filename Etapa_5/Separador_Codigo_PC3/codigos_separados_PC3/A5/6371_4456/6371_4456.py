import math
from numpy import *

vetor = eval(input())

for i in range(size(vetor)):
	if vetor[i] == 0:
		vetor[i] = 81
	else:
		vetor[i] = pow((vetor[i] - 1),2)

print(array(vetor))
		