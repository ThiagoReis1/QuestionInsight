from numpy import*
n = array(eval(input("Digite o numero de alunos matriculados nas turmas: ")))
a = 0
for i in range(size(n)):
	if(n[i]  % 5 == 0):
		a = a + 1
print(a)