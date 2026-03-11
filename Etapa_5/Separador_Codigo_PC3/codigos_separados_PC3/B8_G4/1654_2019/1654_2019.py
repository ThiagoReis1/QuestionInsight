from numpy import *

v= input ("vetor: ").upper().split(',') 
cont = zeros(5,dtype=int)
x=0
for x in range (size(v)):
	if (v[x] == 'AM'):
		cont[0] = cont[0] + 1
	elif (v[x] == 'PE'):
		cont[1] = cont[1] + 1 
	elif (v[x] == 'MG'):
		cont[2] = cont[2] + 1 
	elif (v[x] == 'SP'):
		cont[3] = cont[3] + 1 
	elif (v[x] == 'RS'):
		cont[4] = cont[4]+1		
print(max(cont))
print(cont)
	
