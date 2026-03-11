from numpy import*

turmas = array(eval(input('insira a quantidade de aluno:')))
inpar = 0


for i in range(size(turmas)):
	if turmas[i] % 3 == 0:
		inpar += 1
		
ind = zeros(inpar, dtype='int')
print(inpar)
j = 0
for i in range(size(turmas)):
	if turmas[i] % 3 == 0:
		ind[j] = i
		j += 1
print(ind)
