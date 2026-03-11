from numpy import*
alunos = array(eval(input("entre com as notas:")))
i = 0
reprovados = 0 
vet = zeros(reprovados, dtype=int)
for reprovados in range(size(alunos)):
	if (reprovados[i] < 70):
		reprovados = reprovados + 1
print(reprovados)