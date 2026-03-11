from numpy import*
n= input("nome: ")
i=0
cv=0
cc=0
while i<len(n):
	if n[i]=="A" or n[i]=="E" or n[i]=="I" or n[i]=="O" or n[i]=="U":
		cv=cv+1
		i=i+1
	else:
		cc=cc+1
		i=i+1
v=(cv*0.15)+(cc*0.17)
		
print(round(v,2))