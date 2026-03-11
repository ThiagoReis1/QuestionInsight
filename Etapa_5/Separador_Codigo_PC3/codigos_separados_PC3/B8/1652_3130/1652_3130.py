from numpy import*
from numpy.linalg import*

entrada = input("lalala:").upper()
entrada = entrada.split(',')
cont = zeros(5,dtype=int)
i=0
while(i<len(entrada)):
	if entrada[i]=="B":
		cont[0] = cont[0]+1
	elif entrada[i]=="PA":
		cont[1] = cont[1]+1
	elif entrada[i]=="PR":
		cont[2] = cont[2]+1
	elif entrada[i]=="A":
		cont[3] = cont[3]+1
	elif entrada[i]=="I":
		cont[4] = cont[4]+1	
print
print