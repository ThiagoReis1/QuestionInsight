from numpy import*

palavra=input()
i=0
acum=0
while i< len(palavra):
	if(palavra[i]=="A" or palavra[i]=="E" or palavra[i] == "I" or palavra[i]=="O" or palavra[i]=="U"):
		acum=acum+35.15
	else:
		acum=acum+42.17
	i=i+1

print(round(acum,2))