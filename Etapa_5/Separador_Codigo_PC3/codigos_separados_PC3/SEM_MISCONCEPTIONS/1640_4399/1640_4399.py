from numpy import *
turmas = array(eval(input()))
impar = 0
for i in range(size(turmas)):
	if turmas[i] % 2 != 0:
		impar+=1

turmas_impar = zeros(impar, dtype=int)
j=0
for i in range(size(turmas)):
	if turmas[i] % 2 != 0:
		turmas_impar[j] = i
		j+=1
print(impar)
print(turmas_impar)