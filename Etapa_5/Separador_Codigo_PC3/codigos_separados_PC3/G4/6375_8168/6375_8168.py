from numpy import *

v=input("").upper().split(",")
vz=zeros(4,dtype=int)
for i in v:
	if(i=="A"):
		vz[0]+=1
	elif(i=="B"):
		vz[1]+=1
	elif(i=="C"):
		vz[2]+=1
	else:
		vz[3]+=1
print(vz)