r = input("P/C/A: ").upper()
c = 0
while (r != "X"):
	if (r == "A"):
		c = c + 1
	r = input('P/C/A: ').upper()
print(c)