from numpy import * 
v = zeros(10, dtype= int)
for i in range(10):
	n = int(input())
	if 1 <= n <= 20:
		v[i] = n
		
x=0
minimo = int(input())
for i in v:
	if i >= minimo:
		x +=1
print(x)

alunos = zeros(x, dtype=int)
for i in v:
	if i >= minimo:
		alunos[i] = v[i]
print(alunos)