from numpy import*

vet = array(eval(input("Insira o vetor de alunos:\n")))

qtd = 0

for i in range(size(vet)):
	if(vet[i] % 3 == 0):
		qtd = qtd + 1
saida = zeros(qtd,dtype = int)
for j in range(size(vet)):
	if(vet[j] % 3 == 0):
		for k in range(qtd):
				saida[k] = j
print(qtd)
print(saida)