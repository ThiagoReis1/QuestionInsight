from numpy import*

s = input("").upper()

i = 0 
vogal = 0

while(i < len(s)): 
	if (s[i] == "A") or (s[i] == "E") or (s[i] == "I") or (s[i] == "O") or (s[i] == "U"):
		vogal = vogal + 45.15
	else:
		vogal = vogal + 50.17
	i+=1 
print(round(vogal,2))
		