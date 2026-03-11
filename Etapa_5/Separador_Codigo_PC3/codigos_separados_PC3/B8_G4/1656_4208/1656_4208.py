from numpy import*
pais=input("pais de origem")
v=pais.split(',')
cont=zeros(5,dtype=int)
for i in v:
	if(i=="BE"):
		cont[0]=cont[0]+1
	elif(i=="ES"):
		cont[1]=cont[1]+1
	elif(i=="FR"):
		cont[2]=cont[2]+1
	elif(i=="IT"):
		cont[3]=cont[3]+1
	elif(i=="PT"):
		cont[4]=cont[4]+1
print(max(cont))		
print(cont)
