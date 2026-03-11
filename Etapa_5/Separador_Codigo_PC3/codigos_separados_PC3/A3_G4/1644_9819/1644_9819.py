from numpy import *

alunos = array(eval(input("insira a quantidade de alunos: ")))
acum = zeros(size(alunos), dtype= int)

n = 0

for i in range(size(alunos)):
	if alunos[i] < 5.0:
		n += 1
print(n)

ind = 0
vet = zeros(n)
for i in range(size(alunos)):
	if alunos[i] < 5.0:
		acum[ind] = i
		ind += 1

print(acum)
	
	
