from numpy import*
v=input("string:")

inv=""
cont=0
i=0
while(i<len(v)):
	if(v[i] == "I" and v[i] == "A" and v[i] == "O" and v[i] == "E" and v[i] == "U"):
		v[i]= 0.15
		x=sum(v)
		cont=cont+1
	else:
		v[i]= 0.17
		x=sum(v)
		cont=cont+1
	i=i+1
print(x)