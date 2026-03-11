from numpy import *
vet = array(eval(input("VETOR COM NRO DE ALUNOS EM CADA TURMA:")))
n5 = 0 #ZERA CONTADOR DE CINCOS
j = 0 #CONTADOR PARA O VETOR DE TURMAS COM CINCOS
for i in range(size(vet)): #PERCORRE O VETOR 
	if(vet[i]%5==0): #CONDIÇÃO
		n5 = n5+1 #INCREMENTO
p = zeros(n5,dtype=int) #NOVO VETOR
for i in range(size(vet)):
	if(vet[i]%5==0):
		p[j]=i
		j = j +1
print(n5)
print(p)