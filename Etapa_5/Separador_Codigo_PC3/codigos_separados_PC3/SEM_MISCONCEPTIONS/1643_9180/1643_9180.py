from numpy import*

notas = array(eval(input('Digite as notas dos alunos:')))

quant = 0

for i in range(size(notas)):
	if notas[i] >= 5:
		quant = quant + 1
print(quant)
		
vet = zeros(quant,dtype = int)	
c = 0
		
for i in range(size(notas)):
	if notas[i] >= 5:
		vet[c] = i
		c = c + 1
print(vet)