from numpy import *
turmas = array(eval(input()), dtype=int)

q_imp = 0
for i in turmas:
	if(i % 2 != 0):
		q_imp = q_imp + 1
		
turmas_imp = zeros(q_imp, dtype=int)
aux = 0
for i in range(size(turmas)):
	if(turmas[i] % 2 != 0):
		turmas_imp[aux] = i
		aux = aux + 1
print(q_imp)
print(turmas_imp)