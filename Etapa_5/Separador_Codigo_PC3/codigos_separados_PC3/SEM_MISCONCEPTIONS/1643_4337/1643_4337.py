from numpy import *

notas = array(eval(input("ALUNOS: ")))

aprovados = 0
x = 0

for i in range(size(notas)):
	if(notas[i] >= 5):
		aprovados = aprovados + 1

indices = zeros(aprovados, dtype = int)

for i in range(size(notas)):
	if(notas[i] >= 5):
		indices[x] = i
		x = x + 1
		
print(aprovados)
print(indices)