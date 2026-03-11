from numpy import*
x=(input("x:"))
i=0
y=0
while(len(x)!=i):
	if(x[i]=="A" or x[i]=="E" or x[i]=="I" or x[i]=="O" or x[i]=="U"):
		y=y+0.15
		i=i+1
	else:
		y=y+0.17
		i=i+1
print(round(y,2))
