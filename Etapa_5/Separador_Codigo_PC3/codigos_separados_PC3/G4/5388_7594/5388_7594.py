from numpy import*
l = input().upper()
i = 0
p = 0
while i != len(l):
	if l[i] == "A" or l[i] == "E" or l[i] == "I" or l[i] == "O" or l[i] == "U":
		p += 25.12
	else:
		p += 40.18
	i += 1

print(round(p,2))