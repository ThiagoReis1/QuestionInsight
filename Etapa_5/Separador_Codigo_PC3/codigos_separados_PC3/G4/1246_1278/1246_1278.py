from numpy import *
v1 = array(eval(input("vetor: ")))
a=min(v1)
b=max(v1)
c = 0.75*a+0.25*b
d = 0.25*a+0.75*b
x1=0
x2=0
while (size(v1)>0):
	for i in range(2,size(v1)):
		if (v1[i]>=a and v1[i]<c):
			v1[i] = v1[i]+1
			x1=x1+1
		elif(v1[i]>=c and v1[i]<d):
			v1[i] = v1[i]+1
			x2=x2+1
		else:
			x1=x1+0
x = eval(x1,x2)
print(x)
print(a,b,c,d)

