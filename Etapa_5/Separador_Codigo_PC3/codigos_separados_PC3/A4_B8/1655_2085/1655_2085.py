from numpy import *

vetor = input().split(',')

#incidencia = [0] * 5
incidencia = array(eval('[0,0,0,0,0]'))

for i in range(len(vetor)):
	if (vetor[i] == 'AC'):
		incidencia[0] += 1
	elif (vetor[i] == 'AM'):
		incidencia[1] += 1
	elif (vetor[i] == 'PA'):
			incidencia[2] += 1
	elif (vetor[i] == 'RO'):
			incidencia[3] += 1
	elif (vetor[i] == 'RR'):
			incidencia[4] += 1
	
max = 0
for i in range(len(incidencia)):
	if (incidencia[i] > incidencia[max]):
		max = i
		
print (incidencia[max])
print (incidencia)
