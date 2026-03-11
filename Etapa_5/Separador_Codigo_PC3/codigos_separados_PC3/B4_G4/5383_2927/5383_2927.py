from numpy import *
v= (input("frase: "))


i=0
j=0

while(i < len(v) and i < len(v)):
	if(v[i]=="A"):
		j= j + 0.12
	elif(v[i]=="E"):
		j= j + 0.12
	elif(v[i]=="I"):
		j = j + 0.12
	elif(v[i]=="O"):
		j= j + 0.12
	elif(v[i]=="U"):
		j = j+1
	else:
		j = j + 0.18
	i = i + 1
print(round(j,2))