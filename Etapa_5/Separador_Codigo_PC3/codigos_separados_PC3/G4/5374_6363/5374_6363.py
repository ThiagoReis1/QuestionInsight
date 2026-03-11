from numpy import*

v = input("")
i = 0
j = 0

while(i < len(v)):
	if(v[i].upper() =="A") or (v[i].upper() =="E") or  (v[i].upper() =="I") or  (v[i].upper() =="O") or  (v[i].upper() =="U"):
		j = 0.15 + j
	else:
		j = 0.17 + j
	i = i+1	
print(round(j,2))	


