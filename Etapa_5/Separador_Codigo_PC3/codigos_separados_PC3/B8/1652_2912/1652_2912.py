from numpy import *
string = input()
arr = zeros(5,dtype=int)
string = string.split(',')
for i in string:
	if(i=="PA"):
		arr[1]+=1
	elif(i=="B"):
		arr[0]+=1
	elif(i=="PR"):
		arr[2]+=1
	elif(i=="A"):
		arr[3]+=1
	elif(i=="I"):
		arr[4]+=1
print(max(arr))
print(arr)