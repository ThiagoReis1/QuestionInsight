from numpy import *

turmas = array(eval(input("Alunos: ")))

par = 0
impar = 0
#verificacao par
for i in range(size(turmas)):
	if turmas[i] % 2 == 0:
		par = par + 1
	else:
		impar = impar + 1

j = 0
v_impar = zeros(impar, dtype = int)

for i in range(size(turmas)):
	if turmas[i] % 2 != 0:
		v_impar[j] = i
		j = j + 1

print(impar)
print(v_impar)