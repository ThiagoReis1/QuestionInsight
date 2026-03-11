from numpy import*

cont = zeros(4,dtype = int)
consultorios = input('devidos cunsultorios dos pacientes:').upper().split(',')

for i in consultorios:
	if i == "O":
		cont[0] += 1
	elif i == "D":
		cont[1] += 1
	elif i == "N":
		cont[2] += 1
	elif i == "C":
		cont[3] += 1
print(cont)