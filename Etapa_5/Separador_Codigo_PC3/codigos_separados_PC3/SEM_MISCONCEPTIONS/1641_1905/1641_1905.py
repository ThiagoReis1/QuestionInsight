from numpy import *
v = array(eval(input("")))
turma = 0
vetor = []
i = 0
while i<size(v):
	if v[i]%3==0:
		turma = turma + 1
		vetor.append(i)
	i = i + 1
print(turma)
print(array(vetor))