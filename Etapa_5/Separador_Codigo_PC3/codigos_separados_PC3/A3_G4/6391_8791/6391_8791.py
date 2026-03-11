from numpy import*
r=array(eval(input()))
z=zeros(size(r),dtype=int)
e=0
for i in range(size(r)):
	if r[i]==0:
		z[i]=9**3
	else:
		z[i]=(r[i]-1)**3
print(z)
			