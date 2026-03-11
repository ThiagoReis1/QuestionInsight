from numpy import *
from numpy.linalg import *

entrada = input().upper()
entrada = entrada.split(',')
cont = zeros(5,dtype=int)
i=0
while i<len(entrada):
	if entrada[i] == 'AM':
		cont[0]=cont[0]+1
	elif entrada[i] == 'PE':
		cont[1]= cont[1]+1
	elif entrada[i] == 'MG':
		cont[2]= cont[2]+1
	elif entrada[i] == 'SP':
		cont[3]=cont[3]+1
	elif entrada[i] == 'RS':
		cont[4]=cont[4]+1
	i=i+1
print(max(cont))
print(cont)