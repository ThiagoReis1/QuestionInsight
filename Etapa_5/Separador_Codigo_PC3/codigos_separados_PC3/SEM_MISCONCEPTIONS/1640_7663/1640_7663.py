from numpy import*
turma = array(eval(input("turmas: ")))

j = 0
qturma = 0

for i in range(size(turma)):
	if turma[i] % 2 != 0:
		qturma = qturma + 1
v = zeros(qturma,dtype=int)
for i in range(size(turma)):
	if turma[i] % 2 != 0:
		v[j] = i
		j = j + 1
print(qturma)
print(v)
		