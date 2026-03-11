from numpy import*
v=input("").upper()
i=0
p=0
while(i<len(v)):
	if(v[i]=="A"or v[i]=="E" or v[i]=="I" or v[i]=="O" or v[i]=="U"):
		p=p+0.12
	else:
		p=p+0.18
	i=i+1
	
print(round(p,2))