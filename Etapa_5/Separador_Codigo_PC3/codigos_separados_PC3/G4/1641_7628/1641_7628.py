from numpy import*
a=array(eval(input()))
b=zeros(2,dtype=int)

p=0
for i in range (size(a)):
	if a[i]==3:
		b[0]=b[0]+1
		p=p+1
	elif a[i]!=3:
	   b[1]=b[1]+1
	else:
		b[2]=b[2]+1
print(b)