from numpy import*
v= array(eval(input()))
s=0

for i in range(size(v)):
	if (v[i]%5==0):
		s= s+1
		
v0=zeros(s,dtype=int)
j=0
for i in range(size(v)): 
	if(v[i]%5==0):
		v0[j]= i
		j=j+1
print(s)
print(v0)
	
					
		
