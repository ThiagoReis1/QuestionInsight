from numpy import *

v= array(eval(input("")))
z= array(zeros(2),dtype=int)

c= 0.7*min(v)+0.3*max(v)
d= 0.4*min(v)+0.6*max(v)

x=0
s=0

for i in v:
	if(i>=c and i<d):
		x+=1
	elif(i>=d and i<max(v)):
		s+=1
z[0]=x
z[1]=s
print(z)