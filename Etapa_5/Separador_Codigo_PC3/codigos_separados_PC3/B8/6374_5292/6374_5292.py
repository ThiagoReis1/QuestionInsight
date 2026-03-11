from numpy import*

pacientes = input("digite os pacientes (O)oftamologia,(D)dermatologia,(N)neurologia ,(C)cardiologia:" ).upper().split(",")
qtd = zeros(4, dtype = int)
for i  in range(size(pacientes)):
	if pacientes[i] == "O":
		qtd[0] += 1
	elif pacientes[i] == "D":
		qtd[1] += 1
	elif pacientes[i] == "N":
		qtd[2] += 1
	elif pacientes[i] == "C":
		qtd[3] += 1
print(qtd)