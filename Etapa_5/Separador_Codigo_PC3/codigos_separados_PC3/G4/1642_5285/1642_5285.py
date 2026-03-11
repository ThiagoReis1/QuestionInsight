from numpy import*
#vetor alunos
v = array(eval(input("Digite a quantidade de alunos de cada turma: ")))
#contador pra armazenar
cont = zeros(size(v),dtype=int)
#laco for para valores de v diviseis por 5
for i in v :
	if( v %5 == 0):
		cont[i] = cont[i] + 1

for j in v:
	cont[j] = cont[i]

	
print(nc)	
print(cont)