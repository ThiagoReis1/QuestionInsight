from numpy import*

turma = array(eval(input("Informe o vetor: ")))
qtd = 0

for i in range(size(turma)):
	if(turma[i] % 2 != 0):
		qtd += 1
		
indice = zeros(qtd, dtype = int)
qtd = 0

for i in range(size(turma)):
	if (turma[i] %2 != 0):
		indice[qtd] = i
		qtd += 1
		
print(qtd)
print(indice)


