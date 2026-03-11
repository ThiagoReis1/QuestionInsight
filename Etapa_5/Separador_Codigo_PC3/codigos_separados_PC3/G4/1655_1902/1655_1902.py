from numpy import*
x=input("digite").split(',')

e=zeros(5,dtype= int)

for i in x:
	if(i=="AC"):
		e[0]=e[0]+1
	if(i=="AM"):
		e[1]=e[1]+1
	if(i=="PA"):
		e[2]=e[2]+1
	if(i=="RO"):
		e[3]=e[3]+1
	if(i=="RR"):
		e[4]=e[4]+1
		
print(max(e))
print(e)
	

