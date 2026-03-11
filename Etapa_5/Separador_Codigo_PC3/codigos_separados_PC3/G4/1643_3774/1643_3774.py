from numpy import *

vetor = array(eval(input("Informe os alunos aprovados: ")))
ap = 0

for i in range(size(vetor)):
	if vetor[i] >= 5:
		ap = ap + 1
print(ap)

p = zeros(ap,dtype=int)
j = 0

for i in range(size(vetor)):
	if vetor[i] >= 5:
		p[j] = i	
		j=j+1
print(p)




	
	

	




	
