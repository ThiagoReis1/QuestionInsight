from numpy import *
a = input()
a = a.split(",")
b = array(zeros(5,dtype = int))
for i in range(0,size(a)):
	if(a[i]=="AM"):
		b[0]= b[0]+1
	elif(a[i]=="PE"):
		b[1]= b[1]+1
	elif(a[i]=="MG"):
		b[2]= b[2]+1
	elif(a[i]=="SP"):
		b[3]= b[3]+1
	elif(a[i]=="RS"):
		b[4]= b[4]+1
	
print(max(b))
print(b)
	