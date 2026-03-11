from numpy import*
v=array(eval(input()))
i=0
j=0
r=74.08
while i < size(v):	
	if v[i]<r:
		j+=1
	i+=1	
print(r)		
print(j)

				  
				  