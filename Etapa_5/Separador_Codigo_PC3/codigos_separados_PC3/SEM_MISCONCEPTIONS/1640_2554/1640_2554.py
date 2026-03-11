from numpy import *
turmas=array(eval(input("qntds de alunos matriculados: ")))
impar=0
for i in range(size(turmas)):
	if(turmas[i]%2 != 0):
		impar=impar+1
print(size(turmas)-impar)
cont=zeros(impar,dtype=int)
for i in range(impar):
	if(turmas[i]%2 !=0):
		cont[i]=tu



	

	