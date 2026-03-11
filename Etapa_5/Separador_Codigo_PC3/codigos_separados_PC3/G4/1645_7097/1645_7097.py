from numpy import*
v=array(eval(input("")))
f=0
for i in range(size(v)):
	if v[i]>=2000:
		f=f+1
c=zeros(f,dtype=int)
i=0
for j in range(size(v)):
	if v[j]>=2000:
		c[i]=j
		i+=1
print(f)
print(c)