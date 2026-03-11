from numpy import *
s= input('insira a cor de cabelo:')
y=s.split(',')
x=zeros(5,dtype=int)
for i in y:
	if i=='P':
		x[0]+=1
	elif i=='C':
		x[1]+=1
	elif i=='R':
		x[2]+=1
	elif i=='L':
		x[3]+=1
	elif i=='B':
		x[4]+=1
print(max(x))
print(x)		