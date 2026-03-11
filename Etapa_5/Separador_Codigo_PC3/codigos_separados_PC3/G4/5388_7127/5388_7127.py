from numpy import * 

s = input("Digite a string: ").upper()

i = 0
t = 0

while i < len(s):
	if(s[i] == "A" or s[i] == "E" or s[i] == "I" or s[i] == "O" or s[i] == "U"):
		t = t + 25.12
	else:
		t = t + 40.18
	i = i + 1
print(round(t, 2))		