from numpy import*
v = array(eval(input("tempo:")))

x=max(v)
i=0
s=0
while(i<size(v)):
	if(v[i]==x):
		s=s+1
		print(i)
	i=i+1	
