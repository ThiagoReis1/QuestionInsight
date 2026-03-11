from numpy import *

vet = input(":").lower().split(',')
cont = zeros(5, dtype=int)

for x in vet:
	if(x == 'ac'):
		cont[0] = cont[0] + 1
	elif(x =='am'):
		cont[1] = cont[1] + 1
	elif(x =='pa'):
		cont[2] = cont[2] + 1
	elif(x =='ro'):
		cont[3] = cont[3] + 1
	elif(x =='rr'):
		cont[4] = cont[4] + 1
	else:
		cont[5] = cont[5] + 1
		
print(max(cont))
print(cont)
	
	