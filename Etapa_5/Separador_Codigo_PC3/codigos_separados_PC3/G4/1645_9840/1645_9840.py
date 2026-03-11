from numpy import*
v= array(eval(input("bora la:")))
c=0
for i in v:
	if i>=2000:
		c=c+1
print(c)


z= zeros(c,dtype=int)

s=0
for i in range(size(v)):
	
	if v[i] >=2000:
		
		z[s]=i
		
		s+=1
	
print(z)
		
		
		
