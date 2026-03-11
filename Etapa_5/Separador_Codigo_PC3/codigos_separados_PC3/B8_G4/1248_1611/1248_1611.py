from numpy import*
v=array(eval(input("vetor v:")))
A=min(v)
B=max(v)
C=0.75*A+0.25*B
D=0.25*A+0.75*B

AeC=0
BeD=0
for i in v:
	if i>=C and i<D:
		AeC+=1
	elif i>=D and i<B:
		BeD+=1
x=zeros(2,dtype=int)
x[0]=AeC
x[1]=BeD
print(x)
