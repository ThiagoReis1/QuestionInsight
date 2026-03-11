from numpy import*
r=array(eval(input("")))
z=zeros(size(r),dtype=int)
e=0
for e in range(size(r)):
	if r[e]==9:
		z[e]=0
	else:
		z[e]=(r[e]+1)**2
		e=e+1
print(z)