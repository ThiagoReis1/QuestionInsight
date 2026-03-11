from numpy import*
cont=zeros(5,dtype=int)
e=array(input("estado:").upper().split(','))
for i in e:
	if(i=='AC'):
		cont[0]=cont[0]+1
	elif(i=='AM'):
		cont[1]=cont[1]+1
	elif(i=='PA'):
		cont[2]=cont[2]+1
	elif(i=='RO'):
		cont[3]=cont[3]+1
	elif(i=='RR'):
		cont[4]=cont[4]+1
print(max(cont,key=int))
print(cont)