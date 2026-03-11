from numpy import *
alu = array(eval(input("Digite Alunos: ")))
x = 0

for i in range(size(alu)):
	if (alu[i] % 2 != 0):
		x = x + 1
vet = zeros(x, dtype = int)
y = 0
for j in range(size(alu)):
	if (alu[j] % 2 != 0):
		vet[y] = alu[j]
		y = y + 1
print (vet)	