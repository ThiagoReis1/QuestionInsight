from numpy import *

turmas = array(eval(input()))

par = 0
a = 0

for i in turmas:
	if (i % 2 == 0):
		par = par + 1
		
saida = zeros(par, dtype = int)

for c in range(size(turmas)):
	if (turmas[c] % 2 == 0):
		saida[a] = c
		a = a + 1
		
print (par)		
print (saida)