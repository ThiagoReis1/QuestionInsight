from numpy import*
s = input("").upper()
i = 0
j = 0
while (i < len(s)):
	if (s[i] in "AEIOU"):
		j = j + 1.12
	else: 
		j = j + 1.18
	i = i + 1
print(round(j, 2))
	