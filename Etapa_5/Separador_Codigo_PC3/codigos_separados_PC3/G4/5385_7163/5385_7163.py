s = input("digite a vogal: ").upper()

i = 0
j = 0

while i < len(s):
	if s[i] == "A" or s[i] == "E" or s[i] == "I" or s[i] == "O" or s[i] == "U":
		j = j + 35.15
		i = i + 1
	else:
		j = j + 42.17
		i = i + 1
print(round(j,2))