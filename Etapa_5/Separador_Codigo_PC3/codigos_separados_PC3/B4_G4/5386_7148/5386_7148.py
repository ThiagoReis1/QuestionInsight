from numpy import*

s = input("").upper()

i = 0
j = 0

while(i < len(s)):
	if(s[i] == "A"):
		j = j + 1.12
	elif(s[i] == "E"):
		j = j + 1.12
	elif(s[i] == "I"):
		j = j + 1.12
	elif(s[i] == "O"):
		j = j + 1.12
	elif(s[i] == "U"):
		j = j + 1.12
	else:
		j = j + 1.18
	i = i + 1
print(round(j, 2))
