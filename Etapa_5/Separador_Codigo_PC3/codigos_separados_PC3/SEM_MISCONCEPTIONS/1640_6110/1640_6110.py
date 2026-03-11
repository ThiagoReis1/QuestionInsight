from numpy import*

turma = array(eval(input("Digite a quantidade de turmas: ")))

t = 0

for i in range(size(turma)):
	if(turma[i] % == 0):
		t = t + 1
	
t1 = zeros(t, dtype=int)
t = 0
for i in range(size(turma)):
	if(turma[i] %2 == 0):
		t1[t] = turma[i] + 1
		t = t + 1
print(t1)