from numpy import*

a= array(eval(input("")))

i=1
s=0
g=0
while(i<size(a)):
	g= (a[i-1]-a[i])
	if(g<0):
		s=s -(g)
	else:
		s=s+g
	i=i+1
	
print(s)	
	

	