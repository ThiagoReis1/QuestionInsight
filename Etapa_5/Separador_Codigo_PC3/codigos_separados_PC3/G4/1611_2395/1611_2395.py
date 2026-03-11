from numpy import*
s = input("string: ")
c = 0.0
i = 0
while(i<len(s)):
	if((s[i]=="A") or 
		(s[i]=="E") or 
		(s[i]=="I") or 
		(s[i]=="O") or 
		(s[i]=="U")):
		c = c*0.15
	else:
		c = c*0.17
	i = i + 1
print(round(c,2))
	
	
	