from numpy import *
a=input("Pais:").split(',')
b=len(a)
c=zeros(5, dtype=int)
for i in range(b):
	if (a[i]=="BE"):
		c[0]=c[0]+1
	elif (a[i]=="ES"):
		c[1]=c[1]+1
	elif (a[i]=="FR"):
		c[2]=c[2]+1
	elif (a[i]=="IT"):
		c[3]=c[3]+1
	elif (a[i]=="PT"):
		c[4]=c[4]+1
print(max(c))
print(c)