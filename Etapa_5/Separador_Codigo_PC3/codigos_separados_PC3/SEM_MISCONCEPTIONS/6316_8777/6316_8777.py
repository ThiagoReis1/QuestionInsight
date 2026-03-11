a = input("D,S,I: ").upper()
c = 0
i = 0
while c < len(a):
	if a[c] == "D":
		c += 1
		i += 2.25
	if a[c] == "S":
		c+= 1
		i+= 4.00
	if a[c] == "I":
		c+= 1
		i+= 6.90
	c+=1
	i+=1
print(round(i, 2)c)
