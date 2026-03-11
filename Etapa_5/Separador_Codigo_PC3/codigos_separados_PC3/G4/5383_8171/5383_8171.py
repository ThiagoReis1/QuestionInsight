s=input("")
val=0

for i in range(len(s)):
	if s[i]=="A" or s[i]=="E" or s[i]=="I" or s[i]=="O" or s[i]=="U":
		val+=0.12
	else:
		val+=0.18
print(round(val,2))