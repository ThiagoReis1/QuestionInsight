from numpy import *
from numpy.linalg import *

turmas = array(eval(input("Digite o numero de alunos por turma: ")))

mult = 0

for a in turmas:
	if a%5 == 0:
		mult = mult + 1
t_mult = zeros(mult, dtype=int)
mult2 = 0
for i in range(size(turmas)):
	if turmas[i]%5 == 0:
		t_mult[mult2] = i
		mult2 = mult2 + 1
print(mult)
print(t_mult)
