from numpy import *
n = input(": ").split(',')
cont = zeros(5, dtype = int)
for i in range (size(n)):
	if(n[i] == "AR"):
		cont[0] = cont[0] + 1
	if(n[i] == "BR"):
		cont[1] = cont[1] + 1
	if(n[i] == "CL"):
		cont[2] = cont[2] + 1
	if(n[i] == "CO"):
		cont[3] = cont[3] + 1
	if(n[i] == "UY"):
		cont[4] = cont[4] + 1
print(max(cont))
print(cont)
		