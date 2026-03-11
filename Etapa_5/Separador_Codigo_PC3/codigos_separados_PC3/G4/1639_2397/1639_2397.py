from numpy import*
v=array(eval(input()))
par=0
i=0

while(i<size(v)):
	if((v[i]%2)==0):
		par=par+1
	i=i+1
vr=zeros(par,dtype=int)
j=0
k=0
while(j<size(v)):
	if((v[j]%2)==0):
		vr[k]=j
		k=k+1
	j=j+1
print(par)
print(vr)