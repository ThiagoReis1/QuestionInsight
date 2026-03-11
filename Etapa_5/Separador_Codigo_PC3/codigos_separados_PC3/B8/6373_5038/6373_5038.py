from numpy import*
sequencia = input("sequencia: ").upper().split(',')
cont = zeros(4,dtype=int)
for i in sequencia:
	if(i=="A"):
		cont[0]+=1
	elif(i=="P"):
		cont[1]+=1
	elif(i=="D"):
		cont[2]+=1
	elif(i=="M"):
		cont[3]+=1
print(cont)