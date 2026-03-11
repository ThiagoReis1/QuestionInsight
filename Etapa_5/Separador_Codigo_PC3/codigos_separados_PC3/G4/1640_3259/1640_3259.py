from numpy import *
qa = array(eval(input("Alunos por turma: ")))
imp = 0
k = 0
for i in range(size(qa)):
	if (qa[i] % 2 != 0):
		imp = imp + 1
print(imp)
saida = zeros(imp, dtype=int)
for i in  range(size(qa)):
	if (qa[i] % 2 != 0):
		saida[k] = i
		k = k + 1
print(saida)
		