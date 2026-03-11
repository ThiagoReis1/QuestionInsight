from numpy import*
t_esp = array(eval(input("Tipo de espada: ")))
niv = array(eval(input("Nivel: ")))
i = 0
while(i < size(niv)):
	if(t_esp[i] == "CENOURA"):
		niv[i] = 2 * niv[i]
	elif(t_esp[i] == "FERRO"):
		niv[i] = 4 * niv[i]
	elif(t_esp[i] == "DAEDRIC"):
		niv[i] = 14 * niv[i]
	elif(t_esp[i] == "DWARVEN"):
		niv[i] = 8 * niv[i]
	elif(t_esp[i] == "ELVEN"):
		niv[i] = 11 * niv[i]
	i = i + 1
print(sum(niv))