from numpy import*

apf = array(eval(input('alunos aprovados na disciplina:')))
posi = 0 

for i in range(size(apf)):
	if apf[i] >= 70:
		posi += 1

ind = zeros(posi, dtype = 'int')
print(posi)
ç = 0
for i in range(size(apf)):
	if apf[i] >= 70:
		ind[ç] = i
		ç = ç + 1
print(ind)