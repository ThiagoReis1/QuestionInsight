from numpy import*
v=array(eval(input("Vetores: ")))
A=(min(v))
B=(max(v))
C=((0.7*A)+(0.3*B))
D=((0.4*A)+(0.6*B))
s=zeros(2, dtype=int)
x1=0
x2=0
i=0
while(i<size(v)):
	if(v[i]>=A and v[i]<=C):
		x1=x1+1
	elif(v[i]>=D and v[i]<B):
		x2=x2+1
	i=i+1
s[0]=x1
s[1]=x2
print(s)