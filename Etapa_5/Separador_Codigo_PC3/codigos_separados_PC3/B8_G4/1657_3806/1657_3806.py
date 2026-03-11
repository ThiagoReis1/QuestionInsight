from numpy import*

n= input("estados: ").upper().split(',')

v=zeros(5,dtype=int)

for i in range(size(n)):
	if n[i] =='AZ':
		v[0]=v[0]+1
	elif n[i]== 'CA':
		v[1]=v[1]+1
	elif n[i]== 'FL':
		v[2]=v[2]+1
	elif n[i]== 'PA':
		v[3]=v[3]+1
	elif n[i]== 'WI':
		v[4]=v[4]+1

print (max(v))
print(v)