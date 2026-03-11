from numpy import *
v = array(eval(input("vetor de alunos: ")))

npar = 0
for i in range(size(v)):
	if(v[i] % 2 == 0):
		npar = npar + 1
print(npar)

t = 0
vetor = zeros(npar, dtype=int)

for i in range(0, size(v)):
	if(v[i] % 2 == 0):
		vetor[t] = i
		t = t + 1
print(vetor)

