from numpy import*
cont=zeros(4, dtype=int)
comida=input("tipo de compra:").upper().split(',')
for i in comida:
	if (i=='A'):
		cont[0]=cont[0]+1
	elif (i=='B'):
		cont[1]=cont[1]+1
	elif (i=='L'):
		cont[2]=cont[2]+1
	elif (i=='H'):
		cont[3]=cont[3]+1
print(cont)