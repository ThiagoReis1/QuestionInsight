from numpy import*
v=array(eval(input("")))
j=0
p=0
for i in range(size(v)):
	if(v[i]<5):
		p=p+1

print(p)
v1=zeros(p,dtype=int)
for i in range(size(v)):
	if(v[i]<5):
		v1[j]=i
		j=j+1
		
print(v1)