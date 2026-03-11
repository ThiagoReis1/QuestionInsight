#Lucas Nascimento Estevam da Silva		21602757
#Trabalho Pratico 06
#Exercicio 01

from numpy import*

num = array(eval(input("Numero de alunos: ")))
n = 0

for i in range(size(num)):
	if(num[i] > 0):
		if(num[i] % 2 != 0):
			n = n + 1
vet = zeros(n, dtype = int)
for j in range(size(num)):
	if(num[j] % 2 != 0):
		vet[0 + j] = num[j]
print(n)
print(vet)