s = input("").upper()

i = 0
j = 0

while(i<len(s)):
	if(s[i]=="A"):
		j = j + 35.15
	elif(s[i]=="E"):
		j = j + 35.15
	elif(s[i]=="I"):
		j = j + 35.15
	elif(s[i]=="O"):
		j = j + 35.15
	elif(s[i]=="U"):
		j = j + 35.15
	else:
		j = j + 42.17
	i = i + 1

print(round(j,2))
		