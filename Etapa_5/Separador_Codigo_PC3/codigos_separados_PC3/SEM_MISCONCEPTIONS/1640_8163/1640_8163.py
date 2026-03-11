from numpy import*

vet= array (eval(input("quantidade de alunos: ")))

i=0
cont=0
for i in range(size(vet)):
	if vet[i] % 2 != 0:
		cont=cont+1

for i in range(size(vet)):
	