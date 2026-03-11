from numpy import *
a=input().split(',')
cp=0
cc=0
cm=0
cv=0
ca=0
for i in range(size(a)):
	if(a[i]=='P'):
		cp+=1
	elif(a[i]=='C'):
		cc+=1
	elif(a[i]=='M'):
		cm+=1
	elif(a[i]=='V'):
		cv+=1
	else:
		ca+=1
#b=[cp, cc, cm, cv, ca]
#b=array(cp, cc, cm, cv, ca)
b=zeros(5, dtype=int)
b[0]=cp
b[1]=cc
b[2]=cm
b[3]=cv
b[4]=ca
m=0
for j in range (size(b)):
	if (b[j]>m):
		m=b[j]
print(m)
print(b)
