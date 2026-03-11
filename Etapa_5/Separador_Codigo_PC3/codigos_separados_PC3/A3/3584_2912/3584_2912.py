from numpy import *
arr = array(eval(input()))
i=0
count=0
while(i<size(arr)):
	if(arr[i]>200):
		arr[i] = arr[i]*0.85
	i+=1
print(round(sum(arr),2))