from numpy import *
a = array(eval(input("a:")))
i=0
s=0
while(i!=size(a)):
	if(a[i]>80):
		s=s+a[i]-(a[i]*0.15)
		i=i+1
	else:
		s=s+a[i]
		i=i+1
print(round(s,2))