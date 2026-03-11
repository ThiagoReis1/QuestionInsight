from numpy import *
v=array(eval(input("")))
A=min(v)
B=max(v)
C=0.6 *A + 0.4 * B
D=0.3 * A + 0.7 * B
x=zeros(2,dtype = int)
for i in v:
	if(i >= A and i<C):
		x[0]+=1
	elif(i >= D and i<B):
		x[1]+=1
print(x)