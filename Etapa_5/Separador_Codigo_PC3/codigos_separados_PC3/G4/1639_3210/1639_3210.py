from numpy import*
x=array(eval(input()))
s=0
z=zeros(size(x),dtype=int)

for i in range(size(x)):
	if	(x[i]%2==0):
		s=s+1
for i in range(size(x)):
	if	(x[i]%2==0):
		
		z=z[i]
		

print(s)
print(z)
	
	
	