from numpy import *
cont = zeros(5,dtype=int)
vet = input("quais os estados:").split(",")
for i in (vet):
	if("AM" == i):
		cont[0] = cont[0] + 1
	elif("PE" == i):
		cont[1] = cont[1] + 1
	elif("MG"  == i):
		cont[2] = cont[2] + 1
	elif("SP" == i):
		cont[3] = cont[3] + 1
	elif("RS" == i):
		cont[4] = cont[4] + 1 

print(max(cont))
print(cont)
