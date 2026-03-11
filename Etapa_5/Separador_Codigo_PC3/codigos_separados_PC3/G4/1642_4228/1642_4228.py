from numpy import *
t = array(eval(input("Lista de Alunos: ")))
n = 0
j = 0

for i in range(size(t)):
	if (t[i] % 5 == 0):
		n = n + 1
p = zeros(n, dtype=int)
for i in range(size(t)):
	if (t[i] % 5 == 0): #incremento no vetor
		p[j] = i
		j = j + 1 #variável acumuladora
		
print(n)
print(p)