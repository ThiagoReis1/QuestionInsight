from numpy import *
aulas = array(eval(input("Digite as porcentagem de aulas: ")))
repro = 0
for i in range(size(aulas)):
	if(aulas[i] < 70):
		repro = repro + 1
print(repro)		

indices = zeros (repro, dtype=int)
j= 0

for i in range(size(aulas)):
	if(aulas[i] < 70):
#		print(i)
		indices[j] = i
#		print(i)
		j = j + 1
print(indices)		