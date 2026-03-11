from numpy import*
v=array(eval(input()))
x=0
soma=0
while x!=size(v):
	if v[x]==1:
		soma+=100
	elif v[x]==2:
		soma+=60
	elif v[x]==3:
		soma+=20
	x+=1
print(soma)