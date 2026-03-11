from numpy import*
p=input("p:")
i=0
s=0
while(i!=len(p)):
	if(p[i]=="A" or p[i]=="E" or p[i]=="O" or p[i]=="I" or p[i]=="U"):
		s=s+45.15
		i=i+1
	else:
		s=s+50.17
		i=i+1
print(round(s,2))