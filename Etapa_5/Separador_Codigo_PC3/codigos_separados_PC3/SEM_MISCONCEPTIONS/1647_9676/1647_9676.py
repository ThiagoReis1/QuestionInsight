from numpy import *
aluno = eval(input())
aprov = 0
for i in range(len(aluno)):
	aluno[i] = float(aluno[i])
	if aluno[i] >= 70:
		aprov += 1
print(aprov)
