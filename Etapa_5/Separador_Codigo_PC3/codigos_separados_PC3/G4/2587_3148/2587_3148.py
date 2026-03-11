from numpy import*
v=array(eval(input()))
i=0
l=0
h=v[0]+(v[0]/2)   
for x in v:
	if(x>h):
		print(i)
		i=i+1
		l=l+1
	else:
		i=i+1
print(l)
