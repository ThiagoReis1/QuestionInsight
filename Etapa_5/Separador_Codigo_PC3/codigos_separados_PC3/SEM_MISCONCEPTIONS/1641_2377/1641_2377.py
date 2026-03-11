from numpy import *

turmas = array(eval(input("")))
contadora = 0

for i in range(size(turmas)):
	if turmas[i] % 3 == 0:
		contadora = contadora + 1
c = zeros(contadora, dtype = int)
i = 0
for j in range(size(turmas)):
	if turmas[j] % 3 == 0:
		c[i] = j
		i = i + 1
print(contadora)
print(c)