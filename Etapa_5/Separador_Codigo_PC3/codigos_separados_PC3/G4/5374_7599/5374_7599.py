from numpy import *
lt = input("caractere:").upper()
i = 0
j = 0
while(i<len(lt)):
	if(lt[i]=="A") or (lt[i]=="E") or (lt[i]=="I") or (lt[i]=="O") or (lt[i]=="U"):
		j = j + 0.15
	else:
		j = j + 0.17
	i = i + 1
print(round(j,2))
		
