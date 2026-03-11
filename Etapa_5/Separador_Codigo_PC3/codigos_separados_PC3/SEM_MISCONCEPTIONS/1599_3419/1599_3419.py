from numpy import*
from numpy.linalg import*
vetor = array(eval(input()))
custo = 0
for i in range (size(vetor)):
	if vetor[i]>=80:
		custo+= vetor[i]*0.85
	else:
		custo+= vetor[i]

print(round(custo,2))
