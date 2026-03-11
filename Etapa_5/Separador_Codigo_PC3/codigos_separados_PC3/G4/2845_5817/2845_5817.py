from numpy import*
v=array(eval(input(": ")))
z=zeros(size(v), dtype=int)
for i in range(size(v)):
	if v[i]!=9:
		z[i]=v[i]+1
for i in range(size(v)):
	if v[i]==9:
		z[i]=0

print(z)