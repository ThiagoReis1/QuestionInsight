from numpy import *
v = (input()).upper()
i = 0
vogal = 0
while i < len(v):
	if v[i] == "A" or v[i] == "E" or v[i] == "I" or v[i] == "O" or v[i] == "U":
		vogal = vogal + 1
	i = i + 1
total = (vogal * 0.25) + (i - vogal) * 0.27
print(round(total,2))