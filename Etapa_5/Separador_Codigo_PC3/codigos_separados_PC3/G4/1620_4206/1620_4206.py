from numpy import *
a = array(eval(input()))
b = array(eval(input()))
c = array(zeros(size(a),dtype = float))
t = 0
while(t!=size(a)):
	c[0+t]=a[0+t]*(b[0+t]/20)
	t = t+1
	
print(round(sum(c),2))	