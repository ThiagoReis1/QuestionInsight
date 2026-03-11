from numpy import*
a=0
b=0
c=0
d=0
e=0
v=input("").split(',')
v1=zeros(5,dtype=int)
for i in range(size(v)):
	if(v[i]=="AZ"):
		a=a+1
	elif(v[i]=="CA"):
		b=b+1
	elif(v[i]=="FL"):
		c=c+1
	elif(v[i]=="PA"):
		d=d+1
	elif(v[i]=="WI"):
		e=e+1
	
v1[0]=a
v1[1]=b
v1[2]=c
v1[3]=d
v1[4]=e
print(max(v1))
print(v1)