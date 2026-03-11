from numpy import*
from numpy.linalg import*

vetor = array(eval(input(": ")))
x = size(vetor)
i = 1
a = 0

while i < x:
	if (vetor[i] >= vetor[0]):
		print(i)
		a = a + 1
	i = i + 1
		
print(a)


