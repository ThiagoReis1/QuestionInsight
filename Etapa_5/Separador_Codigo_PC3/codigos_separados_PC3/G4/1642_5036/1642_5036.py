from numpy import *
v = array(eval(input('quantidade de alunos: ')))

cont = 0

for x in v:
	if x % 5 == 0:
		cont += 1
vet = zeros(cont, dtype= int)
x = 0
for i in range(0, size(v)):
	if v[i] % 5 == 0:
		vet[x] = i
		x += 1
		
print(cont)
print(vet)