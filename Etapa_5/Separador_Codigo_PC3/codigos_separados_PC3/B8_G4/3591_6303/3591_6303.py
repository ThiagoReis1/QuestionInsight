from numpy import *
v = array(eval(input()))
p = 0

for i in range(size(v)):
	if v[i]==1 or v[i]==3 or v[i]==5:
		p+=10
	elif v[i]==2 or v[i]==4 or v[i]==6:
		p+=5
print(p)