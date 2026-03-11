from numpy import*

v= input("Informe as nacionalidades: ").upper()

v=v.split(',')

v0= zeros(5,dtype=int)
s=0

for i in range(size(v)):
	if(v[i]=='AR'):
		v0[0]=v0[0]+1
	elif(v[i]=='BR'):
		v0[1]=v0[1]+1
	elif(v[i]=='CL'):
		v0[2]=v0[2]+1
	elif(v[i]=='CO'):
		v0[3]=v0[3]+1
	elif(v[i]=='UY'):
		v0[4]=v0[4]+1

print(max(v0))		
print(v0)
