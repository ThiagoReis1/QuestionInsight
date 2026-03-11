from numpy import *

v= array (eval(input("digite um vetor:")))

a= min(v)
b= max(v)

c=0.75*a+0.25*b
d=0.25*a+0.75*b

z=array(zeros(2,dtype=int))

for i in v:
	if (i>=a and i<c):
		z[0]=z[0]+1
	elif(i>=d and i<b):
		z[1]=z[1]+1
print(z)