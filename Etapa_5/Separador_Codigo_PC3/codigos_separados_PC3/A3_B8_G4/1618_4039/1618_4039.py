from numpy import *
v = 'v'
v1 = "x^"
v2 = "x"
v3 = " + "
f = array(eval(input()))
i=0
c=size(f)
m=c-1
while(i<size(f)-1):
	a=f[i]
	if(f[i]  >= 0 ):
		v = v + str(a) + str(v1) + str(m) + str(v3)
	elif(f[i] == -1 ):
		v = v + str(a) 
	m=m-1
		
	i=i+1
print(v)