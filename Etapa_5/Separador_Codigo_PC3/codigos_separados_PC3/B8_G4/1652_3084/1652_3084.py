from numpy import*
from numpy.linalg import*
x = input().split(',')
y = zeros(5,dtype=int)		 
for i in x:
	if(i == "B"):
		y[0] = y[0]+1
	elif(i == "PA"):
		y[1] = y[1]+1
	elif(i == "PR"):
		y[2] = y[2]+1
	elif(i == "A"):
		y[3] = y[3]+1
	elif(i == "I"):
		y[4] = y[4]+1
z = y.max()
print(z)
print(y)	