from numpy import*
x = array(eval(input("")))
i = 1
c = 0
while(i<size(x)):
	if((x[i])<0 and abs(x[i])>x[0]-x[i]):
		print(i)
		c=c+1
	i = i +1
#	if(x[i]-x[0]):	
print(c)