from numpy import*
v1=array(eval(input()))
v2=zeros(size(v1),dtype=int)
for i in range(size(v1)):
	v2[i]=v1[i]+1
	if v1[i]==9:
		v2[i]=0
print(v2)