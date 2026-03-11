from numpy import *
v1 = array(eval(input("digite os alunos matriculados: ")))
x = 0

for i in range(size(v1)):
	if(v1[i] % 5 == 0):
		x = x + 1
vet = zeros(x, dtype = int)
print(x)

y = 0
for i in range(size(v1)):
	if(v1[i]%5 ==0):
		vet[y]= i
		y = y + 1
print(vet)