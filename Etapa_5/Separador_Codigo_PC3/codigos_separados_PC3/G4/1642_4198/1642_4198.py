from numpy import *
t= array(eval(input("Vetor com numero de alunos de cada turma: ")))

ncinco=  0 #contador de cincos
j=0   #contador para o vetor de turmas com cincos

for i in range(size(t)):
	if(t[i]%5==0):
		ncinco= ncinco + 1
		
#Criacao do vetor das turmas com grupos de cinco
p= zeros(ncinco, dtype=int)
for i in range(size(t)):
	if(t[i]%5==0):
		p[j]= i
		j= j + 1
print(ncinco)
print(p)
	