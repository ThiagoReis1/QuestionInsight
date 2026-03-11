from numpy import *
a = array(eval(input()))
t = 0
b = array(zeros(size(a),dtype = float))
while(t!=size(a)):
	if(a[0+t]>80):
		b[0+t] = a[0+t]-((a[0+t])*15/100)
		t = t+1
	else:
		b[0+t]=a[0+t]
		t = t+1
		
print(round(sum(b),2))		