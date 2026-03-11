from numpy import*

v=zeros(5,dtype=int)
vet=input("").split(',')
for i in vet:
	if i=='AR':
		v[0]=v[0]+1
	elif i=='BR':
		v[1]=v[1]+1
	elif i=='CL':
		v[2]=v[2]+1
	elif i=='CO':
		v[3]=v[3]+1
	elif i=='UY':
		v[4]=v[4]+1
		
print(max(v))
print(v)
		
		