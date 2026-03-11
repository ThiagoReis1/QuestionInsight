from numpy import * 
var = input('').upper().split(',')
cont = zeros(4,dtype = int)

for i in (var):
	if(i=='O'):
		cont[0] = cont[0] + 1		
	if(i=='D'):
		cont[1] = cont[1] + 1
		
	if(i=='N'):
		cont[2] = cont [2] + 1
		
	if(i=='C'):
		cont[3]= cont[3] + 1
							
print(cont)
	

