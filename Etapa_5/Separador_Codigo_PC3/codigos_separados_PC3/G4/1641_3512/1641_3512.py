from numpy import*
alunos= array(eval(input("alunos: ")))
cont = 0	

for i in range (size(alunos)):
	if alunos[i] % 3 == 0:
		cont = cont + 1 
print(cont)
x = zeros(cont,dtype=int)
i=0
	
for cont in range (0, size(alunos)):
	if alunos[cont] % 3 == 0:
		x[i]= cont
		i= i + 1
print(x)

				  