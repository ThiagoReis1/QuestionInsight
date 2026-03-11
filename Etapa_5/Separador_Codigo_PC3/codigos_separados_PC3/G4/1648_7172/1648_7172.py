from numpy import*
x=array(eval(input("oureg:")))
a=0
x1=0
y1=0
for i in range(size(x)):
	if(x[i]<70):
		a=a+1
y=zeros(a,dtype=int)
while(size(x)>x1):
	if(x[x1]<70):
		y[y1]=x1
		x1=x1+1
		y1=y1+1
	else:
		x1=x1+1
print(a)
print(y)
		