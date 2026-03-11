from numpy import*
vetor = array(eval(input("Coloque o numeo de alunos da turma")))
soma = 0

for i in range(size(vetor)):
	if vetor[i] % 3 == 0:
		soma = soma + 1
m = zeros(soma, dtype = int)
h = 0

for j in range(size(vetor)):
	if vetor[j] % 3 == 0:
		m[h] = j
		h = h + 1
print(soma)
print(m)