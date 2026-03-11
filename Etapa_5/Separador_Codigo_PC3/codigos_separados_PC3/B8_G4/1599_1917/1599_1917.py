from numpy import*
x = array(eval(input()))
i = 0
while(size(x)>i):
	if(x[i]>80):
		x[i] = x[i]-(x[i]*0.15)
	elif(x[i]<80):
		x[i] = x[i]
	i = i + 1
print(round(sum(x),2))
