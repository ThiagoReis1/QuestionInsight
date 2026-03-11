from numpy import*

vet= array(eval(input("Insira a quantidade de alunos: ")))
turma=0
for i in range(size(vet)):
	if(vet[i] %5 ==0):
		turma+=1
print(turma)

cont = zeros(turma, dtype=int)
j=0
for i in range(size(vet)):
	if(vet[i] %5 == 0):
		cont[j]=i
		j+=1
print(cont)

		
