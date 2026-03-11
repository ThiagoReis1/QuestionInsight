from numpy import*
x=array(eval(input("x:")))
a=0
b=0
c=0
for i in range(size(x)):
	if(x[i]>=70):
		a=a+1		
y=zeros(a,dtype=int)
while(c!=size(y)):
	if(x[b]>=70):
		y[c]=b
		b=b+1
		c=c+1
	else:
		b=b+1
print(a)
print(y)