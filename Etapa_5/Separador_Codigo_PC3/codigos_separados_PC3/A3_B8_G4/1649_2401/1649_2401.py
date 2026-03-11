from numpy import*
string=input(" ")
string1=string.split(',')
i=0
a=0
b=0
c=0
d=0
e=0
z=0
v=zeros(5,dtype=int)
while(i<len(string)):
	if(string[i]=="P"):
		a=a+1
		
	elif(string[i]=="C"):
		b=b+1
		
	elif(string[i]=="M"):
		c=c+1
		
	elif(string[i]=="V"):
		d=d+1
		
	elif(string[i]=="A"):
		e=e+1
	i=i+1
v[0]=a
v[1]=b
v[2]=c
v[3]=d
v[4]=e
print(max(v))
print(v)
			