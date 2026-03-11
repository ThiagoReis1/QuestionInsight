from numpy import*

vet = array(eval(input("Quantidade de alunos por turma: ")))

cont = 0
for i in range(0, size(vet)):
	if (vet[i]%5 == 0):
		cont+= 1

vec = zeros(cont, dtype = int)
j = 0
for i in range(size(vet)):
	if (vet[i] % 5 == 0):
		vec[j] = i
		j += 1
print(cont)
print(vec)