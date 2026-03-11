from numpy import*
from math import*
v = array(eval(input("Alunos: ")))
pares = 0
i = 0
for x in range(size(v)):
	if (v[i]% 2 == 0):
		pares = pares + 1
	i = i + 1		
u = zeros(pares, dtype = int)

print(pares)
i = 0
j = 0

for x in range(size(v)):
	if (v[i]%2 == 0):
		u[j] = u[j] + i
		j = j + 1
	i = i + 1	
print(u)	
	
