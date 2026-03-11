from numpy import *

#x = [18, 25, 20, 23, 30, 26]

x = array(eval(input("Numero de alunos de cada turma: ")))

grupo = 0
k = 0

for i in range(len(x)):
	if x[i] % 5 == 0:
		grupo += 1
	else:
		pass

v_grupo = zeros(grupo, dtype=int)
	
for j in range(len(x)):
	if x[j] % 5 == 0:
		v_grupo[k] = j
		k += 1
	else:
		pass
		
print(grupo)
print(v_grupo)