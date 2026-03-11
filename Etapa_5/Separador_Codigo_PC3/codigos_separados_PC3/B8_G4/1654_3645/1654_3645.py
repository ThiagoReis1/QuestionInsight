from numpy import *
s= input('insira a string:')
y=s.split(',')
x=zeros(5,dtype=int)
for i in y:
	if i=='AM':
		x[0]+=1
	elif i=='PE':
		x[1]+=1
	elif i=='MG':
		x[2]+=1
	elif i=='SP':
		x[3]+=1
	elif i=='RS':
		x[4]+=1
print(max(x))
print(x)		