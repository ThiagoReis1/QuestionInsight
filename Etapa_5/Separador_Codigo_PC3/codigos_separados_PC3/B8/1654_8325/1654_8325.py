from numpy import*
estado=input("estados: ").upper().split(',')

cont=zeros(5,dtype=int)

for i in range(size(estado)):
	if(estado[i]=="AM"):
		cont[0]=cont[0]+1
	elif(estado[i]=="PE"):
		cont[1]=cont[1]+1
	elif(estado[i]=="MG"):
		cont[2]=cont[2]+1
	elif(estado[i]=="SP"):
		cont[3]=cont[3]+1
	elif(estado[i]=="RS"):
		cont[4]=cont[4]+1
	
print(max(cont))
print(cont)


		