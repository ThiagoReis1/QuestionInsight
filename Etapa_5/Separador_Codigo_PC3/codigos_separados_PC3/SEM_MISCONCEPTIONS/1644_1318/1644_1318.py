from numpy import *

aluno = array(eval(input()))
reprovados = 0

i = 0
while(i < size(aluno)):
	if(aluno[i] < 5.0):
		reprovados = reprovados + 1
	i = i + 1
print(reprovados)
i = 0
j = 0
tmp = ones(reprovados, dtype=int)
while(i < size(aluno)):
	if(aluno[i] < 5.0):
		tmp[j] = i
		j = j + 1
	i = i + 1
print(tmp)
