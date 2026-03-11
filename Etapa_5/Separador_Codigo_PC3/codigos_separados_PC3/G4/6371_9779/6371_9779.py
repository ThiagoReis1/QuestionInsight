from numpy import*
v=array(eval(input()))
z=zeros(size(v), dtype=int)

for i in range(size(v)):
	if v[i]==0:
		z[i]=9**2
	else:
		z[i]=(v[i]-1)**2
print (z)