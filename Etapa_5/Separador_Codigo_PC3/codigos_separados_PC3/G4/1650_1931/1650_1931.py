from numpy import*
x=input("digite").split(',')

e=zeros(5,dtype= int)

for i in x:
	if(i=="P"):
		e[0]=e[0]+1
	if(i=="C"):
		e[1]=e[1]+1
	if(i=="R"):
		e[2]=e[2]+1
	if(i=="L"):
		e[3]=e[3]+1
	if(i=="B"):
		e[4]=e[4]+1
		
print(max(e))
print(e)
	

