from numpy import*
from numpy.linalg import*

x= input("").split(',')
cont= zeros(5,dtype=int)

for x in x:
	if(x=="AC"):
		cont[0]=cont[0]+1
	elif(x=="AM"):
		cont[1]=cont[1]+1
	elif(x=="PA"):
		cont[2]=cont[2]+1
	elif(x=="RO"):
		cont[3]=cont[3]+1
	elif(x=="RR"):
		cont[4]=cont[4]+1
	
print(max(cont))
print(cont)