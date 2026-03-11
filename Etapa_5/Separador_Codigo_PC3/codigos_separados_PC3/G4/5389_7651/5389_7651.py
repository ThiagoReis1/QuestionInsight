from numpy import*
v = input().upper()
i = 0
c = 0
b = len(v)
while (i < b):
	if (v[i] == "A" or v[i] == "E" or v[i] == "I" or v[i] == "O" or v[i] == "U"):
		c = c + 3.15
	else:
		c = c + 4.17
	i += 1	
print (round(c, 2))		