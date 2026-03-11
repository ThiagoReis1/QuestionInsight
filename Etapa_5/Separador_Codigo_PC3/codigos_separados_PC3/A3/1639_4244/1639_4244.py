from numpy import*

#Vetores
numeros = array(eval(input("Numero de alunos por turma: ")))

#Zeros
par = zeros(1, dtype = int)
k = zeros(2, dtype = int)

#Laco for e if
for i in numeros:
	if(i % 2 == 0):
		par[0] = par[0] + 1
print(par)
for j in range(0, size(numeros)):
	if(j % 2 != 0):
		k = numeros[i % 2]
print(k)
		
		