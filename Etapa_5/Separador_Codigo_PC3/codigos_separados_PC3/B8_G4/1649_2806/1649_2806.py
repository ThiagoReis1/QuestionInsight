from numpy import *

x=input("").split(',')
y=zeros(5,dtype=int)


for i in range(size(x)):
	if(x[i] == "P"):
		y[0] += 1
	elif(x[i] == "C"):
		y[1] += 1
	elif(x[i] == "M"):
		y[2] += 1
	elif(x[i] == "V"):
		y[3] += 1
	elif(x[i] == "A"):
		y[4] += 1
		
print(max(y))
print(y)
