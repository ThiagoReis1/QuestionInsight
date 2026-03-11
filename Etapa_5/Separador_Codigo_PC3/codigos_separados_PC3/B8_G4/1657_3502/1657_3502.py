from numpy import*
x= input("").split(',')
cont= zeros(5,dtype=int)

for x in x:
	if(x=="AZ"):
		cont[0]=cont[0]+1
	elif(x=="CA"):
		cont[1]=cont[1]+1
	elif(x=="FL"):
		cont[2]=cont[2]+1
	elif(x=="PA"):
		cont[3]=cont[3]+1
	elif(x=="WI"):
		cont[4]=cont[4]+1
print(max(cont))
print(cont)