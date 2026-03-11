from numpy import *
v= input('').split(',')

cont= zeros(4, dtype=int)
for i in v:
	if(i == 'E'):
		cont[0]= cont[0] +1
	if(i == 'V'):
		cont[1]= cont[1] +1
	if(i == 'A'):
		cont[2]= cont[2] +1
	if(i == 'D'):
		cont[3]= cont[3] +1
print(cont)