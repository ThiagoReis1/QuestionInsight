from numpy import *
atd = input("Informe qual seu atendimento: ").upper().split(',')
vetor = zeros(4,dtype = int)
for i in range(len(atd)):
	if atd[i] == "O":
		vetor[0] = vetor[0]+1
	elif atd[i] == "D":
		vetor[1] = vetor[1]+1
	elif atd[i] == "N":
		vetor[2] = vetor[2]+1
	elif atd[i] == "C":
		vetor[3] = vetor[3]+1
		
print(vetor)