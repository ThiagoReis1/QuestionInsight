from numpy import*
c= array(eval(input()))
b=0
while(b<size(c)):
	if(c[b]==max(c)):
		print(b)
	b=b+1