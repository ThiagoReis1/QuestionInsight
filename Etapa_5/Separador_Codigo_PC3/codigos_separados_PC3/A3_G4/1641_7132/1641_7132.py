from numpy import *

vet = array(eval(input("quantidade de alunos matriculos: ")))

cont = 0
resultado = zeros(size(vet), dtype=int)

for i in range(size(vet)):
	if vet[i] % 3 == 0:
		cont = cont + 1

r = 0
vt = zeros(cont, dtype=int)

for i in range(size(vet)):
	if vet[i] % 3 == 0:
		vt[r] = i
		r = r + 1
		
	
print(cont)
print(vt)