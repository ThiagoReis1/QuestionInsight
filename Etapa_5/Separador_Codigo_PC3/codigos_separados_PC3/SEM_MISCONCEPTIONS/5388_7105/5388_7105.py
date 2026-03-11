from numpy import *
i = 0
custo = 0
s = input().upper()

while(i<len(s)):
	if(s[i] == "A" or s[i] == "E" or s[i] == "I" or s[i] == "O" or s[i] == "U"):
		custo +=25.12
	else:
		custo += 40.18
	i+=1
print(round(custo,2))