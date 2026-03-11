from numpy import *
v=array(eval(input()))
i=0
p=0
while i<size(v):
	if v[i]== 1 or v[i]==6:
		p=p+10
	elif v[i]==2 or v[i]==4:
		p=p+5
	elif v[i]==3:
		p=p
	elif v[i]==5:
		p=p+20
	i+=1
print(p)