from numpy import *
arr = array(eval(input()))
count = 0
for i in range(size(arr)):
	if(arr[i]<70):
		count+=1
arr2 = ones(count,dtype=int)
count = 0
for i in range(size(arr)):
	if(arr[i]<70):
		arr2[count] = i
		count+=1
print(count)
print(arr2)