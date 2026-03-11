from numpy import *
from numpy.linalg import *

turmas=array(eval(input()))

qtd_mult = 0
for ele in turmas:
	if ele%5 == 0:
		qtd_mult += 1
		
turmas_mult = zeros(qtd_mult,dtype = int)
qtd_mult = 0
for i in range(size(turmas)):
	if turmas[i]%5 == 0:
	   turmas_mult[qtd_mult] = i
	   qtd_mult += 1
	
print(qtd_mult)
print(turmas_mult)