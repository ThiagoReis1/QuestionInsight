# Hanna Soares Rodrigues - 21650885

from numpy import*

vetor = array(eval(input("Digite o vetor: ")))

a = min(vetor)
b = max(vetor)
c = (0.75*a) + (0.25*b)
d = (0.25*a) + (0.75*b)

x = zeros(2,dtype=int)

for i in range(size(vetor)):
	if (vetor[i] >= a) and (vetor[i] < c): 
		x[0] = x[0] + 1
	if (vetor[i] >= d) and (vetor[i] < b): 
		x[1] = x[1] + 1
	
print(x)