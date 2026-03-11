from numpy import * 

x = input().upper()

i = 0
total = 0

while(i<len(x)):
	if((x[i]=="A") or (x[i]=="E") or (x[i]=="I") or (x[i]=="O") or (x[i]=="U")):
		total = total + 45.12 
	else:
		total = total + 50.18
	i = i + 1
print(round(total, 2))
		
	

