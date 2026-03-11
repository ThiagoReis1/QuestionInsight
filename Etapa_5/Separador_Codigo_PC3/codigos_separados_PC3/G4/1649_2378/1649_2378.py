from numpy import*

c=input().split(',')

e=zeros(5,dtype=int)

for i in c:
	if(i=="P"):
		e[0]=e[0]+1
	if(i=="C"):
		e[1]=e[1]+1
	if(i=="M"):
		e[2]=e[2]+1
	if(i=="V"):
		e[3]=e[3]+1
	if(i=="A"):
		e[4]=e[4]+1
		
print(max(e))
print(e)