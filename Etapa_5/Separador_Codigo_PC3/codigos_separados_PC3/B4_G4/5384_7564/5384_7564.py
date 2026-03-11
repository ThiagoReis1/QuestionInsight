from numpy import*
st = input("").upper()
x=0
i=0
while(i<len(st)):
	if(st[i]=="A"):
		x=x+45.15
	elif(st[i]=="E"):
		x=x+45.15
	elif(st[i]=="I"):
		x=x+45.15
	elif(st[i]=="O"):
		x=x+45.15
	elif(st[i]=="U"):
		x=x+45.15
	else:
		x=x+50.17
	i=i+1
print(round(x,2))


