from numpy import*
s = input("digite uma palavra: ").upper()
i = 0
tt= 0
tt1 = 0
while(i<len(s)):
	if(s[i]=="A" or s[i]=="E" or s[i]=="I" or s[i]=="O" or s[i]=="U"):
		tt = tt + 0.19
	else:
		tt = tt + 0.23
	i = i +1
print(round(tt,2))