from numpy import *
a = array(eval(input()))
t = 0
for i in range(0,size(a)):
	if(a[i]%5==0):
		t = t+1
	
b = array(zeros(t,dtype = int))
x = 0
for i in range(0,size(a)):
	if(a[i]%5==0):
		b[x]= b[x]+i
		x = x+1

print(t)
print(b)