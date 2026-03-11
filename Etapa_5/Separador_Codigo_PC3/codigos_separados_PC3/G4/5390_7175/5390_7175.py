eti=input("etiqueta:  ")
i=0
sm=0
while(i<len(eti)):
	if(eti[i]=="A" or eti[i]=="E" or eti[i]=="I" or eti[i]=="O" or eti[i]=="U"):
		sm=sm+0.19
	else:
		sm=sm+0.23
	i=i+1

print(round(sm, 2))