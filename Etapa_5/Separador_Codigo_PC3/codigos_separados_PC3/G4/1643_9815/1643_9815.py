from numpy import *

v = array(eval(input("Insira a nota dos alunos: ")), dtype=float)
cont = 0

for i in range(size(v)):
	if v[i] >= 5.0:
		cont += 1

print(cont)
v0 = zeros(cont, dtype=int)
j = 0

for i in range(size(v)):
	if v[i] >= 5.0:
		v0[j] = i
		j += 1

print(v0)