from numpy import *

qam = array(eval(input("Digite a quantidade de alunos matriculados: ")))

qi = 0 # contador da quantidade impar

for i in qam:
	if (i % 2 != 0):
		qi = qi + 1

cqi = zeros(qi, dtype=int)
ii = 0

for i in range (size(qam)):
	if (qam[i] % 2 != 0):
		cqi[ii] = i
		ii = ii + 1

print(qi)
print(cqi)