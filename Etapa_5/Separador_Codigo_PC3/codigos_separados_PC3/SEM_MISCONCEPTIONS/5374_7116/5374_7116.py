from numpy import*

rt = input(": ").upper()
vogal = 0.15
carac = 0.17
i = 0
acum = 0

while i < len(rt):
	if rt[i] == "A" or rt[i] == "E" or rt[i] == "I" or rt[i] == "O" or rt[i] == "U":
		acum = acum + vogal
	else:
		acum = acum + carac
	i = i + 1
print(round(acum, 2))