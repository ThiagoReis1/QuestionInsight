from numpy import *
v=array(eval(input("")))
q=0
for x in v:
	if x%3==0:
		q+=1
u=zeros(q,dtype=int)
j=0
for i in range(size(v)):
	if v[i]%3==0:
		u[j]=i
		j+=1
print(q)
print(u)
		