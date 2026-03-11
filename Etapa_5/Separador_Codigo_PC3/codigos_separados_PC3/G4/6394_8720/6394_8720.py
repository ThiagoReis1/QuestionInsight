from numpy import*
v=array(eval(input()))
v2=zeros(size(v), dtype=int)
for i in range(size(v)):
	if v[i]==9:
		v2[i]=0
	else:
		v2[i]=v[i]+1
print(v2)
		