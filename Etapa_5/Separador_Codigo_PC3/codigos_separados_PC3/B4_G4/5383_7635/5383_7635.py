from numpy import*

s = input("palavra:").upper()
i = 0 
l = 0
while(l < len(s)):
	if(s[l] == "A"):
		i = i + 0.12
	elif(s[l] == "E"):
		i = i + 0.12
	elif(s[l] == "I"):
		i = i + 0.12
	elif(s[l] == "O"):
		i = i + 0.12
	elif(s[l] == "U"):
		i = i + 0.12
	else:
		i = i + 0.18
		
	l = l + 1
print(round(i , 2 ))