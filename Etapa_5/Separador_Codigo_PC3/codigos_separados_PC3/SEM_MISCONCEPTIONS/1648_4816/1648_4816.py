from numpy import *

n = array(eval(input()))

reprovados = 0

for i in range(size(n)):
	if n[i] < 70:
		reprovados += 1

print(reprovados)

indice = zeros(reprovados,dtype=int)
j = 0

for i in range(size(n)):
	if n[i] < 70:
		indice[j] = i
		j += 1
		
print(indice)


	