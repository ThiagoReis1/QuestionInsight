from numpy import*
v=array(eval(input()))
t=0
for x in v:
	if(x%3==0):
		t=t+1
print(t)
#v 2 tem q ter os indices
v2=zeros(t,dtype=int)
i=0
a=0
while(i<size(v) and a<size(v2)):
	if(v[i]%3==0):
		v2[a]=i
		a=a+1
	i=i+1
print(v2)

		
		
	
