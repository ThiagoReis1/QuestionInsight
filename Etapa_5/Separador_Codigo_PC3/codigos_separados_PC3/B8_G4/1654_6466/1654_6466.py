from numpy import*
e= input("Estado: ").split(',')
v=zeros(5,dtype=int)

for c in range (size(e)):
	if e[c]=='AM':
		v[0]=v[0]+1
	elif e[c]=='PE':
		v[1]=v[1]+1
	elif e[c]=='MG':
		v[2]=v[2]+1
	elif e[c]=='SP':
		 v[3]=v[3]+1
	elif e[c]=='RS':
		v[4]=v[4]+1
print(max(v))
print(v)