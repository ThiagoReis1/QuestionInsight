from numpy import*
from numpy.linalg import*

entrada = input("d:").upper()
entrada = entrada.split(',')
cont = zeros(5,dtype=int)
i=0

while i <len(entrada):
	if entrada[i]=="CNH":
		cont[0]=cont[0]+1
	elif entrada[i]=="JPN":
		cont[1] = cont[1]+1
	elif entrada[i]=="KOR":
		cont[2] = cont[2]+1
	elif entrada[i]=="MLG":
		cont[3] = cont[3]+1
	elif entrada[i]=="THA":
		cont[4] = cont[4]+1
print(cont[i])  
print(cont)
	
