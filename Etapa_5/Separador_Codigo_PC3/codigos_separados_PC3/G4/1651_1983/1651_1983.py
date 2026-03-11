from numpy import*
x=input("digite").split(',')

e=zeros(6,dtype= int)

for i in x:
	if(i=="MC"):
		e[0]=e[0]+1
	if(i=="C"):
		e[1]=e[1]+1
	if(i=="CM"):
		e[2]=e[2]+1
	if(i=="EM"):
		e[3]=e[3]+1
	if(i=="E"):
		e[4]=e[4]+1
	if(i=="ME"):
		e[5]=e[5]+1
print(max(e))
print(e)