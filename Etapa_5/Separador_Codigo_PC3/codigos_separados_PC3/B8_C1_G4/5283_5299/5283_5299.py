n = int(input(""))
c = 0
s = 0
while (n != 0):
	if (n > 0):
		c = c + 1
		n = int(input(":"))
	elif (n < 0):
		s = s +1
		n = int(input("/"))
	if (n == 0):
		a = c + s
		x = c*100/a
print(a)
print(round(x, 2))