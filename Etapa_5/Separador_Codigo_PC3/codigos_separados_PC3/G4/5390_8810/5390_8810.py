n = input().upper()
s = 0
for i in range(len(n)):
	if n[i] == "A" or n[i] == "E" or n[i] == "I" or n[i] == "O" or n[i] == "U":
		s = s + 0.19
	else:
		s = s + 0.23
print(round(s,2))