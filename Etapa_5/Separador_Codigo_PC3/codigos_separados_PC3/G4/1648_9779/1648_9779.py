from numpy import*
v=array(eval(input()))
a=0
for i in range(size(v)):
	if v[i]<70:
		a+=1
print(a)
z=zeros(a, dtype=int)
b=0
for i in range(size(v)):
	if v[i]<70:
		z[b]=i
		b+=1
print(z)