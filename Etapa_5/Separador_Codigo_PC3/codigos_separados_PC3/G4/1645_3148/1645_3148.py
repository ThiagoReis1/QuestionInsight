from numpy import*
v=array(eval(input()))
i=0

for x in v:
	if(x >=2000):
		i=i+1
print(i)	
z=zeros(i,dtype=int)
b=0
c=0
for j in v:
	if(j>=2000):
		z[c]=z[c]+b
		b=b+1
		c=c+1
	else:
		b=b+1
print(z)
		
		
		
	
		