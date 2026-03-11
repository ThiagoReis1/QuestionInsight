from numpy import *
e=input("Digite a entrada:").split(',')
vt=zeros(6,dtype=int)
for j in range(size(e)):
	if (e[j] == "MC"):
		vt[0]=vt[0]+1
	elif (e[j] == "C"):
		vt[1]=vt[1]+1
	elif (e[j] == "CM"):
		vt[2]=vt[2]+1
	elif (e[j] == "EM"):
		vt[3]=vt[3]+1
	elif (e[j] == "E"):
		vt[4]=vt[4]+1
	elif (e[j] == "ME"):
		vt[5]=vt[5]+1
print(max(vt))
print(vt)