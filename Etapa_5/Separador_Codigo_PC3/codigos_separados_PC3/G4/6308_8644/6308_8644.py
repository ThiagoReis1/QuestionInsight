s = input("").upper()
i = 0
v = 0
c1 = 0
c2 = 0
c3 = 0

while(i < len(s)):
	if(s[i] == "A"):
		v = v + 16.75
		c1 = c1 + 1
	if(s[i] == "L"):
		v = v + 4.60
		c2 = c2 + 1
	if(s[i] == "P"):
		v = v + 2.85
		c3 = c3 + 1
	i = i + 1
print(round(v, 2), c1,c2,c3)