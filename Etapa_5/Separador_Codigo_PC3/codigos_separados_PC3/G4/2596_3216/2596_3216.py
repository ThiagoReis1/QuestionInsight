from numpy import*
v= array(eval(input()))

for i in range(size(v)):
	c=1
	if(v[i]>=v[0]):
		c= c+1
		print(c)