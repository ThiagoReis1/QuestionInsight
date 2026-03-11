from numpy import *

q = array(eval(input("Digite a quantidade de alunos: ")))
i = 0
t = 0

for i in range(size(q)):
	if(q[i] % 5 == 0):
		t = t + 1
print(t)
	
N = zeros(t, dtype = int)
entrada = 0
saida = 0

for i in range(size(q)):
	if(q[i] % 5 == 0):
		N[entrada] = i
		entrada = entrada + 1
print(N)