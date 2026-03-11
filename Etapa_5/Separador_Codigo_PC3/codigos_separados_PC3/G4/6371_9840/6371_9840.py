from numpy import*
v= array(eval(input("manda la:")))
z=zeros(size(v),dtype=int)
for i in range(size(v)):
	if v[i]!=0:
		z[i]=z[i]+(v[i]-1)**2
	else:
		z[i]=z[i]+9**2
print(z, end=" ")