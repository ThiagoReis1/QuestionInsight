from numpy import*
paciente = input().upper().split(",")
aux = zeros(4, dtype = int)
for i in range(0,size(paciente)):
	if paciente[i] == "O":
		aux[0] += 1
	elif paciente[i] == "D":
		aux[1] += 1
	elif paciente[i] == "N":
		aux[2] += 1
	elif paciente[i] == "C":
		aux[3] += 1
print(aux)
	