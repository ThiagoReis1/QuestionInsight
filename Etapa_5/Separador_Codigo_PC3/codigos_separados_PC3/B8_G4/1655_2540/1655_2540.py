from numpy import *

E = input("estados").split(",")
cont = zeros(5, dtype=int)

for i in range(size(E)):
	if(E[i] == "AC"):
		cont[0] = cont[0] + 1
	elif(E[i] == "AM"):
		cont[1] = cont[1] + 1
	elif(E[i] == "PA"):
		cont[2] = cont[2] + 1
	elif(E[i] == "RO"):
		cont[3] = cont[3] + 1
	elif(E[i] == "RR"):
		cont[4] = cont[4] + 1
		
print(max(cont))
print(cont)
		