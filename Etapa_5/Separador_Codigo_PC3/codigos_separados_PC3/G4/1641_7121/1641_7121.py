from numpy import *

turma = array(eval(input()))
a = 0

for i in range(size(turma)):
	if turma[i] % 3 == 0:
		a = a + 1
x = zeros(a, dtype = int)
y = 0

for i in range(size(turma)):
	if turma[i] % 3 == 0:
		x[y] = i
		y = y + 1

print(a)
print(x)