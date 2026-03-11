from numpy import *

reprovados = 0 
alunos = array(eval(input()))
for elemento in alunos:
	if elemento < 70:
		reprovados += 1
	
print(reprovados)

el = 0
z = zeros(reprovados, dtype=int)
reprovados = 0
for el in range(size(alunos)):
	if alunos[el] < 70:
		z[reprovados] = el
		reprovados += 1
		
	
print(z)