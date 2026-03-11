from numpy import*
v = input("frase").upper()
i =0
j= 0
while(i <len(v)):
	if(v[i]=="A"):
		j=j+35.15
	elif(v[i]=="E"):
		j=j+35.15
	elif(v[i]=="I"):
		j=j + 35.15
	elif(v[i]=="O"):
		j=j+35.15
	elif(v[i]=="U"):
		 j=j+35.15
	else:
		j=j+42.17
	i=i+1
print(round(j,2))
