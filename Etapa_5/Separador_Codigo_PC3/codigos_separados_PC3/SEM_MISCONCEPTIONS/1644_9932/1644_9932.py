from numpy import*
notas = eval(input())
aluno = 0
l = []
for i in range(len(notas)):
	if notas[i] < 5:
		l.append(i)
		aluno += 1
l = array(l)	
print(aluno)
print(l)