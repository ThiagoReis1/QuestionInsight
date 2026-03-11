from numpy import*
v=input("v: ").upper().split(',')


c=zeros(5, dtype=int)
for i in range(size(v)):
	if v[i]=='BE':
		c[0]=c[0]+1
		e=e+1
	elif v[i]=='ES':
		c[1]=c[1]+1
		e=e+1
	elif v[i]=='FR':
		c[2]=c[2]+1
		e=e+1
	elif v[i]=='IT':
		c[3]=c[3]+1
		e=e+1
	elif v[i]=='PT':
		c[4]=c[4]+1
		e=e+1
print(max(c))
print(c)