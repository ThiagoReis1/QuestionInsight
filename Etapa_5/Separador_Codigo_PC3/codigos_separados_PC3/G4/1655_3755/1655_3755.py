from numpy import *
v=input('Estados:').upper()
x=v.split(',')
z=zeros(5,dtype=int)
for i in range(size(x)):
	if x[i]=='AC':
		z[0]=z[0]+1
	elif x[i]=='AM':
		z[1]=z[1]+1
	elif x[i]=='PA':
		z[2]=z[2]+1
	elif x[i]=='RO':
		z[3]=z[3]+1
	else:
		z[4]=z[4]+1
print(max(z))
print(z)