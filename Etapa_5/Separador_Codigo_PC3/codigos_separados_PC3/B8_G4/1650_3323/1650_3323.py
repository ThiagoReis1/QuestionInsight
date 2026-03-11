from numpy import*
from numpy.linalg import*
a=input("Entrada: ").split(',')
i=0
cont=zeros(5,dtype=int)

for i in range (size(a)):
	if(a[i]=="P"):
		cont[0]=cont[0]+1
	elif(a[i]=="C"):
		cont[1]=cont[1]+1
	elif(a[i]=="R"):
		cont[2]=cont[2]+1
	elif(a[i]=="L"):
		cont[3]=cont[3]+1
	elif(a[i]=="B"):
		cont[4]=cont[4]+1	
print(max(cont))
print(cont)


