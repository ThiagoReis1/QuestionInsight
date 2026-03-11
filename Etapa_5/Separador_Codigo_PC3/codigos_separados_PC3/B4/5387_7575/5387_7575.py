from numpy import*

p=(input("digite uma palavra: ").upper())

i=0
total=0

while i<len(p):
	if(p[i]=="A"):
		total=total+45.12
	elif(p[i]=="E"):
		total=total+45.12
	elif p[i]=="I":
		total=total+45.12
	elif p[i]=="O":
		total=total+45.12
	elif p[i]=="U":
		total=total+45.12
	else:
		total=total+50.18
	i=i+1

print(round(total,2))