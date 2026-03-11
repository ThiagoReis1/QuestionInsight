from numpy import*
s = input("")
for i in s:
	if s[i] == "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
		inv = s[i].upper()
		print(inv)
	else:
		inv = s[i].lower()
		print(inv)