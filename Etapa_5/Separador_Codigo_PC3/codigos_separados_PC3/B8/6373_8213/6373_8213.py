from numpy import*
vetor=input("digite>>>>").split(",")
vv=zeros(4,dtype=int)

for i in range(size(vetor)):
	if (vetor[i]=="A"):
		vv[0]=vv[0]+1
	elif (vetor[i]=="P"):
		vv[1]=vv[1]+1
	elif (vetor[i]=="D"):
		vv[2]=vv[2]+1
	elif (vetor[i]=="M"):
		vv[3]=vv[3]+1
print(vv)
		