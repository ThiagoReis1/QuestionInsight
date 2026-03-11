from numpy import*

A=input("estados: ").split(',')
b=0
c=0
d=0
e=0
f=0
for i in range (size(A)):
	if(A[i]=="AZ"):
		b=b+1
	if(A[i]=="CA"):
		c=c+1
	if(A[i]=="FL"):
		d=d+1
	if(A[i]=="PA"):
		e=e+1
	if(A[i]=="WI"):
		f=f+1
print(max(b,c,d,e,f))
		

v=array([b,c,d,e,f])
print(v)
