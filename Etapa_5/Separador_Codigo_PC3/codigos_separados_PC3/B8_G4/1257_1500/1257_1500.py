from numpy import*
v=array(eval(input("bota vetor:")))
A=min(v)
B=max(v)
C=0.85*A + 0.15*B
D=0.4*A + 0.6*B
AeC=0
BeD=0
for i in v:
	if i>=A and i<C:
		AeC=AeC+1
	elif i>=D and i<B:
		BeD=BeD+1
x=zeros(2,dtype=int)
x[0]=AeC
x[1]=BeD
print(x)