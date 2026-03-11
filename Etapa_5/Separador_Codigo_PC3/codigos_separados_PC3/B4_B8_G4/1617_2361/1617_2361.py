from numpy import *
TE = array(eval(input("Tipo da Espada: ")))
TC = array(eval(input("Nível do Combate: ")))
i = 0
while (i < size(TE)):
	if (TE[i] == "CENOURA"):
		 TE[i] = 2
	elif (TE[i] == "FERRO"):
		 TE[i] = 4
	elif (TE[i] == "DWARVEN"):
		 TE[i] = 8
	elif (TE[i] == "ELVEN"):
		 TE[i] = 11
	elif (TE[i] == "DAEDRIC"):
		 TE[i] = 4
	i = i + 1
j = 0
while (j < size(TE)):
	TE = (TE[j]*TC[j])
	j = j + 1
print (sun(TE))