from numpy import *

cont= zeros(5, dtype=int) 
vet = input("ESTADO: ").upper().split(',') 

for x in vet:
	if(x == 'AM'): 
		cont[0] = cont[0] + 1 
	elif(x == 'PE'): 
		cont[1] = cont[1] + 1 
	elif(x == 'MG'): 
		cont[2] = cont[2] + 1 
	elif(x == 'SP'):
		cont[3] = cont[3] + 1 
	elif(x == 'RS'):
		cont[4] = cont[4] + 1 
print(max(cont))
print(cont)