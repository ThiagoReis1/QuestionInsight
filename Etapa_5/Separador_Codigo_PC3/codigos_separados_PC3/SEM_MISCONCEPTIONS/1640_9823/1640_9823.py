from numpy import*

alunos = array(eval(input()))
cont = 0

for i in range(0, size(alunos)):
	if alunos[i]%2 != 0:
		cont = cont + 1

vetor = zeros(cont, dtype=int)
y = 0
for i in range(0, size(alunos)):
	if alunos[i]%2 != 0:
		vetor[y] = i
		y = y + 1

print(cont)
print(vetor)