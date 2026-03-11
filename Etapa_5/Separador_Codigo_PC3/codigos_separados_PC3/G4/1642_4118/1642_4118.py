from numpy import*
turma = array(eval(input("qtd de alunos: ")))
qt = 0
for el in turma:
	if(el%5 == 0):
		qt += 1
z = zeros(qt, dtype = int)
p = 0
for i in range(len(turma)):
	if(turma[i]%5 == 0):
		z[p] = i
		p+=1
		
print(qt)
print(z)
	