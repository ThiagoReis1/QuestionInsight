from numpy import* 

s = input(" ").upper()
i = 0
c = 0
while i in range(len(s)):
	if s[i] == 'E':
		c += 1
	i = i + 1
print(c)