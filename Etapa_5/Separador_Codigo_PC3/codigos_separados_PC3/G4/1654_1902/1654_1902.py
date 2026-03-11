from numpy import*
x=input("digite").split(',')

e=zeros(5,dtype= int)

for i in x:
	if(i=="AM"):
		e[0]=e[0]+1
	if(i=="PE"):
		e[1]=e[1]+1
	if(i=="MG"):
		e[2]=e[2]+1
	if(i=="SP"):
		e[3]=e[3]+1
	if(i=="RS"):
		e[4]=e[4]+1
		
print(max(e))
print(e)
	

