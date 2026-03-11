from numpy import *

n = array(eval(input("Notas: ")))
i = 0   #indice do vetor
p = 0
acul = 0

while (i < size(n)):
	n[i] = n[i]*(p+1)
	acul = acul + n[i]
	i = i + 1
	p = p + 1
print(acul)
print(round((acul/size(n)), 2))