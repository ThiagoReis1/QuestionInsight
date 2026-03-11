from numpy import *
v=input(" ").split(',')
c=zeros(5,dtype= int)
for i in range (size(v)):
	if (v[i]=="B"):
		c[0]=c[0]+1
	elif (v[i]=="PA"):
		c[1]=c[1]+1
	elif (v[i]=="PR"):
		c[2]=c[2]+1
	elif (v[i]=="A"):
		c[3]=c[3]+1
	elif (v[i]=="I"):
		c[4]=c[4]+1
print(max(c))
print(c)
	
		
	
