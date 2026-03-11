from numpy import *

tom_pele = input().split(',')
vetor = zeros(6, dtype=int)
for i in tom_pele:
	if(i == 'MC'):
		vetor[0] += 1
	elif(i == 'C'):
		vetor[1] += 1
	elif(i == 'CM'):
		vetor[2] += 1
	elif(i == 'EM'):
		vetor[3] += 1
	elif(i == 'E'):
		vetor[4] += 1
	else:
		vetor[5] += 1
print(max(vetor))
print(vetor)
