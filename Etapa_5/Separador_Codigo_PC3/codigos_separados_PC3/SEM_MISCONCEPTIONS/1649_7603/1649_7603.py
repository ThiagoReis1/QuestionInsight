from numpy import *

cor = array(input(" ").upper()

cont = 0

for i in range(len(cor)):
	if cor[i] == "P":
		cont[0] = cont[0] + 1
	elif cor[i] == "C":
		cont[1] = cont[1] + 1 
	elif cor[i] == "M":
		cont[2] = cont[2] + 1
	elif cor[i] == "V":
		cont[3] = cont[3] + 1
	else:
		cont[4] = cont[4] + 1
	
print(max(cont))
print(cont)