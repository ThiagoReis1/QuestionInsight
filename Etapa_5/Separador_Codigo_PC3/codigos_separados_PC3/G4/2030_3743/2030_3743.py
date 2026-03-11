face = input()
c = 0
a = 0
while face.upper() != "S":
	if face.upper() == "CARA":
		a = a + 1
		c = c + 1
		face = input()
	else:
		c = c + 1
		face = input()
print(a)
	