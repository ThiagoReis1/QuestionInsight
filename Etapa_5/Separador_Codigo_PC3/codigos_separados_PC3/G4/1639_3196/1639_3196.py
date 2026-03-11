from numpy import*
vet = array(eval(input('qtd de alunos por turma: ')))

cont = 0

for i in range(0, size(vet)):
	if vet[i]%2 == 0:
		cont += 1
		

g = zeros(cont, dtype=int)


i2 = 0

for j in range (0, size(g)):
	if (vet[j]%2) == 0:
		
		g[i2] = vet[j]
		
		i2 += 1
		
print(cont)
print(g)
		

		
