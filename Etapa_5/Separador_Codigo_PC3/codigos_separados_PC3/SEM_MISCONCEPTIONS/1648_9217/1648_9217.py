from numpy import *

vetor = array(eval(input("Digite os valores dos indices de frequencia: ")))
reprovados = 0


for i in range(size(vetor)):
	if vetor[i] < 70:
		reprovados = reprovados + 1

j=0	
n = zeros(reprovados,dtype = int)
for i in range(size(vetor)):
	if vetor[i] < 70:
		n[j] = i
		j = j + 1
		

print(reprovados)
print(n)