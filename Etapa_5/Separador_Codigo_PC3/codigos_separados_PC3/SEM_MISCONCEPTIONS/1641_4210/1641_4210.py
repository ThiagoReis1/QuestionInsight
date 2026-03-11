from numpy import*
alunos = array(eval(input("alunos: ")))

n = 0

for i  in alunos:
	if(i%3 == 0):
		n = n + 1
turma = zeros(n,dtype=int)
j = 0

for x in range(size(alunos)):
	if(alunos[x]%3==0):
		turma[j] = x
		j = j + 1
print(n)
print(turma)