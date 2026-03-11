from numpy import *

q = array(eval(input("Informe a quantidade de alunos matriculados: ")))

i = 0
u = 0


for x in range(0, size(q)):
	if q[x]%3==0:
		i = i + 1
	v = zeros(i, dtype=int)
	
for x in range(0, size(q)):
	if q[x]%3==0:
		v[u] = x
		u = u + 1
		
print(i)
print(v)
