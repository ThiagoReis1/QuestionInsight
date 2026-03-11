from numpy import *
MQ = input("digite a string: ").split(',')
c= zeros(5, dtype = int)
for i in range (size(MQ)):
	if(MQ[i]=="AZ"):
		c[0]=c[0]+1
	elif(MQ[i]=="CA"):
		c[1]=c[1]+1	
	elif(MQ[i]=="FL"):
		c[2]=c[2]+1
	elif(MQ[i]=="PA"):
		c[3]=c[3]+1	
	elif(MQ[i]=="WI"):
		c[4]=c[4]+1			
print(max(c))
print(c)