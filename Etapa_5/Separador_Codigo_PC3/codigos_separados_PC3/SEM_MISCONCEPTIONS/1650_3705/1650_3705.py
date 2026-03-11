from numpy import*
vetor=input("").split(',')

i=0
np=0
nc=0
nm=0
nv=0
na=0
tt=zeros(5,dtype=int)
while(i<size(vetor)):
	for x in vetor:
		if(x=="P"):
			np=np+1
			tt[0]=np
		elif(x=="C"):
			nc=nc+1
			tt[1]=ncnp=np+1
			tt[0]=np
		elif(x=="C"):
			nc=nc+1
			tt[1]=nc
		elif(x=="R"):
		elif(x=="R"):
			nm=nm+1
			tt[2]=nm
		elif(x=="L"):
			nv=nv+1
			tt[3]=nv
		elif(x=="B"):
			na=na+1
			tt[4]=na
		i=i+1
	i=i+1
print(max(tt))
print(tt)
	



