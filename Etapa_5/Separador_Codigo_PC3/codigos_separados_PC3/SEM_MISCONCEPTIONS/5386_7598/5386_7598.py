from numpy import*

s = input("senha: ").upper()
i = 0
total = 0

while(i<len(s)):
	if(s[i] == "A") or (s[i] == "E") or (s[i] == "I") or (s[i] == "O") or (s[i] == "U"):
		total = total + 1.12
		
	else:
		total = total + 1.18

	i = i + 1

print(round(total,2))

