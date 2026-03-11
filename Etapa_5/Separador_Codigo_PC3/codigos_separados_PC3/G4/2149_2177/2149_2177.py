from numpy import *
v=array(eval(input("")))
v1=array(eval(input("")))
s=zeros(size(v))
for i in range (size(s)):
	s[i]=v[i]+v1[i]
print(s)
u=0
for j in range (size(s)):
	if s[j]>=12.0:
			u=u+1
print(u)
	
	
	
	
	
	
			
			