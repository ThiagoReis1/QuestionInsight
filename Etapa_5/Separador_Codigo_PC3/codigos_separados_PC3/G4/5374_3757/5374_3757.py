p=input(":0")
i=0
v=0
while(i!=len(p)):
	if(p[i]=="A" or p[i]=="E" or p[i]=="I" or p[i]=="O" or p[i]=="U"):
		v=v+0.15
		i=i+1
	else:
		v=v+0.17
		i=i+1
print(round(v,2))