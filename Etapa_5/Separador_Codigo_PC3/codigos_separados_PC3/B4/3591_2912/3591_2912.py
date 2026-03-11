from numpy import *
arr = array(eval(input()))
i=0
count=0
while(i<size(arr)):
	if(arr[i]==1):
		count+=10
	elif(arr[i]==2):
		count+=5
	elif(arr[i]==3):
		count+=10
	elif(arr[i]==4):
		count+=5
	elif(arr[i]==5):
		count+=10
	else:
		count+=5
	i+=1
print(count)