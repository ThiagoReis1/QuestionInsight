from numpy import*
v=array(eval(input()))
k=size(v)
x=zeros(k, dtype=int)
c=0
for i in v:
	if i==9:
		x[c]=0
	else:
		x[c]=(i+1)**3
	c+=1
print(x)