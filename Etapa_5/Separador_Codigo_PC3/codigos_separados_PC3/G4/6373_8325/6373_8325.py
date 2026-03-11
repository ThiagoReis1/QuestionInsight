from numpy import*

s=input("sequencia: ").upper().split(',')

cont=zeros(4,dtype=int)

for i in size(len(cont)):
	if(s[i]=="A"):
		cont[0]=cont[0]+1
	elif(s[i]=="P"):
		cont[1]=cont[1]+1
	elif(s[i]=="D"):
		cont[2]=cont[2]+1
	else:
		cont[3]=cont[3]+1
	print(s)