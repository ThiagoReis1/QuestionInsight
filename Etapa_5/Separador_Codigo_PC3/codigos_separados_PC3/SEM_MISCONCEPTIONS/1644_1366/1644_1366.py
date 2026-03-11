from numpy import *

cont = 0
contReprovados = 0

notas = array(eval(input()))

for nota in notas:
	if nota < 5:
		contReprovados = contReprovados + 1
	
	cont = cont + 1

cont = 0
contNotas = 0
reprovados = zeros(contReprovados, dtype=int)
for nota in notas:
	if nota < 5:
		reprovados[cont] = contNotas
		cont = cont + 1
	
	contNotas = contNotas + 1

print(contReprovados)
print(reprovados)