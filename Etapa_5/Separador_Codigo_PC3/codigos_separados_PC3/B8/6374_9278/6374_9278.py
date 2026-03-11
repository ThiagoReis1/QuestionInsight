from numpy import*

especialidades = input("digite: ").upper().split(",")
resultado = zeros(4, dtype = int)

for i in range(size(especialidades)):
	if especialidades [i] == "O":
		resultado[0]+=1
	elif especialidades [i] == "D":
		resultado[1]+=1
	elif especialidades [i] == "N":
		resultado[2]+=1
	elif especialidades [i] == "C":
		resultado[3]+=1
print(resultado)