from numpy import*
t = array(eval(input("vetor com numero de alunos de cada turma: ")))

ncinco = 0 #zera contador de cincos
j = 0 #contador para o vetor de turmas com cinco

for i in range(size(t)):
	if(t[i] % 5 == 0):
		ncinco = ncinco + 1
			
p = zeros(ncinco, dtype=int)

for i in range(size(t)):
	if(t[i]%5 == 0):
		p[j] = i
		j = j + 1

print(ncinco)
print(p)