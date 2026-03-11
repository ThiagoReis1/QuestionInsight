from numpy import *
from numpy.linalg import *

entrada= input().upper()
entrada= entrada.split(',')

cont= zeros(6, dtype=int)
i=0
while i < len(entrada):
	if entrada[i] == 'AZ':
		cont[0]= cont[0] + 1
	elif entrada[i] == 'CA':
		cont[1]= cont[1] + 1
	elif entrada[i] == 'FL':
		cont[2]= cont[2] + 1
	elif entrada[i] == 'PA':
		cont[3]= cont[3] + 1
	elif entrada[i] == '':
		cont[4]= cont[4] + 1
	elif entrada[i] == 'ME':
		cont[5]= cont[5] + 1
	i=i+1	
print(max(cont))
print(cont)