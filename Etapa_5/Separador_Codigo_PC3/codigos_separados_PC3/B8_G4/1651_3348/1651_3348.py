from numpy import*
from numpy.linalg import*

a = input().split(',')
b = zeros(6, dtype= int)

for i in range(len(a)):
	if(a[i]=="MC"):
		b[0] += 1
	elif(a[i]=="C"):
		b[1] += 1
	elif(a[i]=="CM"):
		b[2] += 1
	elif(a[i]=="EM"):
		b[3] += 1
	elif(a[i]=="E"):
		b[4] += 1
	elif(a[i]=="ME"):
		b[5] += 1
print(max(b))
print(b)