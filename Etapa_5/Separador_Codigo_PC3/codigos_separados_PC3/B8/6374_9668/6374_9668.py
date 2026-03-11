from numpy import * 

especialidade = input("especialidade: ").upper().split(',')
atendimento= zeros(4, dtype = int)

for i in range(size(especialidade)):
	if especialidade[i] == "O":
		atendimento[0] = atendimento[0] + 1
	elif especialidade[i] == "D":
		atendimento[1] = atendimento[1] + 1
	elif especialidade[i] == "N":
		atendimento[2] = atendimento [2] + 1
	elif especialidade[i] == "C":
		atendimento[3] = atendimento[3] + 1

print(atendimento)