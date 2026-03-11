sn=input("senha:  ")
i=0
vs=0
while(i<len(sn)):
	if(sn[i].upper()=="A" or sn[i]=="E" or sn[i]=="I" or sn[i]=="O" or sn[i]=="U"):
		vs=vs+3.15
	else:
		vs=vs+4.17
	i=i+1

print(round(vs, 2))