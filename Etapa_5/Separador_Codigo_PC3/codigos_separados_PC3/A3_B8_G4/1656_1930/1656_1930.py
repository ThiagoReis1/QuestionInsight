from numpy import*

s= input().split(',')

cont=zeros(5,dtype=int)
t=0
for i in s:
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
t=max(cont)
print(t)
print(cont)
		