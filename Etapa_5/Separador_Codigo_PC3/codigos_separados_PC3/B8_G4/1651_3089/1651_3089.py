from numpy import*
v1=input().split(",")
v=v1

s2=zeros(6,dtype=int)

for i in range(size(v)):
	if(v[i]=="MC"):
		s2[0]=s2[0]+1
	elif(v[i]=="C"):
		s2[1]=s2[1]+1
	elif(v[i]=="CM"):
		s2[2]=s2[2]+1
	elif(v[i]=="EM"):
		s2[3]=s2[3]+1
	elif(v[i]=="E"):
		s2[4]=s2[4]+1
	elif(v[i]=="ME"):
		s2[5]=s2[5]+1
print(max(s2))
print(s2)		
