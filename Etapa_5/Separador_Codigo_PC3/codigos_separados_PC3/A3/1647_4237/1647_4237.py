from numpy import*
x=array(eval(input("Aluno: ")))

alunos = 0 
aprovado = 0

for i in range(size(x)):
	if(x[i] >= 70):
		alunos = alunos + 1
		print(alunos)
		
vet = zeros(alunos, dtype=int)
					
for y in range(size(x)):
	if(x[y]>=70):
		vet[y] = y
		
print(vet)