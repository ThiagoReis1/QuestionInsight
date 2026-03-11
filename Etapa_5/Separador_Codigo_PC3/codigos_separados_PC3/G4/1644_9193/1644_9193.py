from numpy import *

v = array(eval(input("Digite o vetor de notas: ")))

c = 0
y = 0
for i in range(size(v)):
	if v[i] < 5:
		c += 1
		
v1 = zeros(c, dtype=int)

for x in range(size(v)):
	if v[x] < 5:
		v1[y] = x
		y += 1
print(c)
print(v1)