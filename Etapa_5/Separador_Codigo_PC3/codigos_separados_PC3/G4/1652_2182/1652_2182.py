from numpy import *

vet = input(":").lower().split(',')
cont = zeros(5, dtype=int)

for x in vet:
	if(x == 'b'):
		cont[0] = cont[0] + 1
	elif(x =='pa'):
		cont[1] = cont[1] + 1
	elif(x =='pr'):
		cont[2] = cont[2] + 1
	elif(x =='a'):
		cont[3] = cont[3] + 1
	elif(x =='i'):
		cont[4] = cont[4] + 1
	else:
		cont[5] = cont[5] + 1
	
print(max(cont))
print(cont)