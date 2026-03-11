from numpy import*
v=array(eval(input()))
A=min(v)
B=max(v)
C=0.75*A + 0.25*B
D=0.25*A + 0.75*B
x=zeros(2,dtype=int)
i=0
while(i<size(v)):
	for i in range(0,size(v)):
		if(v[i]>=A and v[i]<C):
			x[0]=x[0]+1
		elif(v[i]>=C and v[i]<D):
			x[1]=x[1]+1
	i=i+1
print(x)