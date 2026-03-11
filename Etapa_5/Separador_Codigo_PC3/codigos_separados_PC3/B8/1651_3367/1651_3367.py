from numpy import *
from numpy.linalg import *

entrada= input().upper()
entrada= entrada.split(',')

cont= zeros(6, dtype=int)
i=0
while i < len(entrada):
	if entrada[i] == 'MC':
		cont[0]= cont[0] + 1
	elif entrada[i] == 'C':
		cont[1]= cont[1] + 1
	elif entrada[i] == 'CM':
		cont[2]= cont[2] + 1
	elif entrada[i] == 'EM':
		cont[3]= cont[3] + 1
	elif entrada[i] == 'E':
		cont[4]= cont[4] + 1
	elif entrada[i] == 'ME':
		cont[5]= cont[5] + 1
	i=i+1	
print(max(cont))
print(cont)