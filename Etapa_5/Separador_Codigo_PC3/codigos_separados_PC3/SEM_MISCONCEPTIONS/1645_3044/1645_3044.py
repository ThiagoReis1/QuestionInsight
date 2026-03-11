from numpy import*
x=array(eval(input("vetor: ")))
s=0
for i in range(0,size(x)):
	if(x[i]>=2000):
		s=s+1
print(s)
z=zeros(s,dtype=int)
for j in range(size(x)):
print(z)