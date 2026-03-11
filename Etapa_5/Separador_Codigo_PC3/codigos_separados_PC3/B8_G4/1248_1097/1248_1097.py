from numpy import*
v1=array(eval(input("digite o vetor:")))
v=zeros(2, dtype=int)
A=min(v1)
B=max(v1)
C=((0.75*A)+(0.25*B))
D=((0.25*A)+(0.75*B))
for i in range(size(v1)):
	if(v1[i]>=C and v1[i]<D):
		v[0]=v[0]+1
	elif(v1[i]>=D and v1[i]<B):
		v[1]=v[1]+1
print(v)