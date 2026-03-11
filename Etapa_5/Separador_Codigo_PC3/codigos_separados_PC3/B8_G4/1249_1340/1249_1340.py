from numpy import*
v=array(eval(input("vetor v:")))
A=min(v)
B=max(v)
C = 0.7 * A + 0.3 * B
D = 0.4 * A + 0.6 * B
AeC=0
BeD=0
for i in v:
	if i>=A and i<C:
		AeC+=1
	elif i>=C and i<D:
		BeD+=1
x=zeros(2,dtype=int)
x[0]=AeC
x[1]=BeD
print(x)