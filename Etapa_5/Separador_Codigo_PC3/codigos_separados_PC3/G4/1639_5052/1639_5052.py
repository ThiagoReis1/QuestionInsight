from numpy import *
v=array(eval(input("Vetor: ")))

c=0

for i in range(size(v)):
	if v[i]%2==0:
		c=c+1
print(c)

u=zeros(c, dtype=int)
j=0

for i in range(size(v)):
	if v[i]%2==0:
		u[j]=i
		j=j+1
print(u)
