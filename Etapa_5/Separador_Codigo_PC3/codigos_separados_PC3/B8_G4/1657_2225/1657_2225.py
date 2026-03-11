from numpy import*

v=input("v: ").upper().split(',')
x=zeros(5, dtype=int)

for i in range(len(v)):
	if v[i]=='AZ':
		x[0]=x[0]+1
	elif v[i]=='CA':
		x[1]=x[1]+1
	elif v[i]=='FL':
		x[2]=x[2]+1
	elif v[i]=='PA':
		x[3]=x[3]+1
	elif v[i]=='WI':
		x[4]=x[4]+1
print(max(x))
print(x)