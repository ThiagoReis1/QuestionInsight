from numpy import *
turmas=array(eval(input("turmas: ")))
acum=0
for i in range(size(turmas)):
	if turmas[i] % 2 == 0:
		cont=cont+1
print(cont)

