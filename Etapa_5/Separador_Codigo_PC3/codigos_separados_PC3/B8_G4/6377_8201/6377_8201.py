from numpy import*
e=input().upper().split(",")
s=zeros(4,dtype=int)
for i in range(len(e)):
	if e[i]=="A":
		s[0]+=1
	elif e[i]=="B":
		s[1]+=1
	elif e[i]=="C":
		s[2]+=1
	elif e[i]=="D":
		s[3]+=1
print(s)