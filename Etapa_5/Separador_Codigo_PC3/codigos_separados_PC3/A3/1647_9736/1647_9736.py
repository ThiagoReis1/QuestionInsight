from numpy import*

alunos = array(eval(input()))
cont = 0
j = 0

for i in range(0, size(alunos)):
	if alunos[i] >= 70:
		cont = cont + 1
		
vetor = zeros(cont, dtype = int)
j = 0
for i in range(0, size(alunos)):
	if alunos[i] >= 70:
		vetor[j] = i
		j = j + 1
		
print(cont)
print(vetor) 