from numpy import*
t=input("Tons de pele: ").split(',')
z=zeros(6,dtype=int)

for i in range(size(t)):
	if t[i]=='MC':
		z[0]=z[0]+1
	if t[i]=='C':
		z[1]=z[1]+1
	if t[i]=='CM':
		z[2]=z[2]+1
	if t[i]=='EM':
		z[3]=z[3]+1
	if t[i]=='E':
		z[4]=z[4]+1
	if t[i]=='ME':
		z[5]=z[5]+1
		
print(max(z))
print(z)