# O = aftalmologia; D dermatologia; N Neurologia; C cardiologia
from numpy import*
pacientes = input("Tipo de paciente: ").upper()
count = zeros(4, dtype = int)
for i in pacientes:
	if (i == "O"):
		count[0] = count[0] + 1
	elif (i == "D"):
		count[1] = count[1] + 1
	elif(i == "N"):
		count[2] = count[2] + 1
	elif (i == "C"):
		count[3] = count[3] + 1
print(count)