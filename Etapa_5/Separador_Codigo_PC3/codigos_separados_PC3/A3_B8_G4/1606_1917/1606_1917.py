from numpy import*
x = array(eval(input()))
i = 0
while(size(x)>i):
	if(x[i]<x[i+1]):
		y = x[i+1]-x[i]
	elif(x[i]>x[i+1]):
		y = x[i]-x[i+1]
	i = i + 1
print(int(sum(x)))